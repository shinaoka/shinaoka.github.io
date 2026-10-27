#!/usr/bin/env python3
"""Collect GitHub statistics for the Software page.

Reads _data/software.yml and writes _data/software_stats.json.
Needs a GitHub token in GITHUB_TOKEN (or GH_TOKEN); only public data is used.
"""

import datetime as dt
import fnmatch
import json
import os
import pathlib
import sys
import urllib.request

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONFIG = ROOT / "_data" / "software.yml"
OUTPUT = ROOT / "_data" / "software_stats.json"
ACTIVITY_DAYS = 90

REPO_FIELDS = """
fragment R on Repository {
  nameWithOwner
  description
  url
  homepageUrl
  isArchived
  isFork
  isPrivate
  stargazerCount
  primaryLanguage { name }
  issues(states: OPEN) { totalCount }
  pullRequests(states: OPEN) { totalCount }
  latestRelease { tagName publishedAt url }
  defaultBranchRef {
    target {
      ... on Commit {
        committedDate
        history(since: $since) { totalCount }
      }
    }
  }
}
"""


def graphql(query, variables):
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN or GH_TOKEN is required")
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = json.load(resp)
    if body.get("errors"):
        sys.exit(f"GraphQL error: {json.dumps(body['errors'], indent=2)}")
    return body["data"]


def fetch_org(org, since):
    query = REPO_FIELDS + """
    query($org: String!, $since: GitTimestamp!, $after: String) {
      organization(login: $org) {
        repositories(first: 50, privacy: PUBLIC, isFork: false, after: $after,
                     orderBy: {field: NAME, direction: ASC}) {
          pageInfo { hasNextPage endCursor }
          nodes { ...R }
        }
      }
    }
    """
    repos, after = [], None
    while True:
        data = graphql(query, {"org": org, "since": since, "after": after})
        conn = data["organization"]["repositories"]
        repos += conn["nodes"]
        if not conn["pageInfo"]["hasNextPage"]:
            return repos
        after = conn["pageInfo"]["endCursor"]


def fetch_repos(names, since):
    if not names:
        return []
    parts = []
    for i, name in enumerate(names):
        owner, repo = name.split("/")
        parts.append(f'r{i}: repository(owner: "{owner}", name: "{repo}") {{ ...R }}')
    query = REPO_FIELDS + "query($since: GitTimestamp!) {\n" + "\n".join(parts) + "\n}"
    data = graphql(query, {"since": since})
    return [data[f"r{i}"] for i in range(len(names)) if data[f"r{i}"]]


def summarize(node):
    commit = (node.get("defaultBranchRef") or {}).get("target") or {}
    release = node.get("latestRelease")
    return {
        "name": node["nameWithOwner"],
        "description": node.get("description") or "",
        "url": node["url"],
        "homepage": node.get("homepageUrl") or "",
        "language": (node.get("primaryLanguage") or {}).get("name", ""),
        "stars": node["stargazerCount"],
        "open_issues": node["issues"]["totalCount"],
        "open_prs": node["pullRequests"]["totalCount"],
        "last_commit": (commit.get("committedDate") or "")[:10],
        "commits_recent": (commit.get("history") or {}).get("totalCount", 0),
        "release": release["tagName"] if release else "",
        "release_date": (release["publishedAt"] or "")[:10] if release else "",
        "release_url": release["url"] if release else "",
    }


def is_excluded(name, patterns):
    short = name.split("/")[1].lower()
    return any(fnmatch.fnmatch(short, p.lower()) for p in patterns)


def main():
    config = yaml.safe_load(CONFIG.read_text())
    now = dt.datetime.now(dt.timezone.utc)
    since = (now - dt.timedelta(days=ACTIVITY_DAYS)).strftime("%Y-%m-%dT%H:%M:%SZ")

    nodes = []
    for org in config.get("orgs", []):
        nodes += fetch_org(org, since)
    nodes += fetch_repos(config.get("repos", []), since)

    excludes = config.get("exclude", [])
    repos = {}
    for node in nodes:
        if node["isPrivate"] or node["isArchived"] or is_excluded(node["nameWithOwner"], excludes):
            continue
        repos[node["nameWithOwner"].lower()] = summarize(node)

    categories = []
    for cat in config.get("categories", []):
        entries = [repos.pop(name.lower()) for name in cat.get("repos", []) if name.lower() in repos]
        if entries:
            categories.append({"title": cat["title"], "links": cat.get("links", []), "repos": entries})
    if repos:
        others = sorted(repos.values(), key=lambda r: (-r["stars"], r["name"].lower()))
        categories.append({"title": "Other repositories", "links": [], "repos": others})

    result = {
        "generated_at": now.strftime("%Y-%m-%d %H:%M UTC"),
        "activity_days": ACTIVITY_DAYS,
        "categories": categories,
    }

    # Skip rewriting when only the timestamp would change, to avoid empty daily commits.
    if OUTPUT.exists():
        old = json.loads(OUTPUT.read_text())
        old.pop("generated_at", None)
        if old == {k: v for k, v in result.items() if k != "generated_at"}:
            print("No changes")
            return
    OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
