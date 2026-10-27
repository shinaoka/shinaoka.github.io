---
title: Software
layout: single
classes: wide
---

{% assign stats = site.data.software_stats %}

Open-source software developed by our group and collaborators.
The statistics below are collected from GitHub every day
(last update: {{ stats.generated_at }}).
"Commits" counts commits to the default branch in the last {{ stats.activity_days }} days.

* [Hiroshi Shinaoka's personal repositories](https://github.com/shinaoka)
* [SpM-lab](https://github.com/SpM-lab) / [tensor4all](https://github.com/tensor4all)

<style>
  .sw-table { font-size: 0.8em; }
  .sw-table td, .sw-table th { vertical-align: top; }
  .sw-table td.num, .sw-table th.num { text-align: right; white-space: nowrap; }
  .sw-desc { display: block; color: #6f777d; }
  .sw-idle { color: #9aa1a6; }
  .sw-release { white-space: nowrap; }
</style>

{% for cat in stats.categories %}
{% if cat.title == "Other repositories" %}
<details markdown="0">
<summary><strong>{{ cat.title }} ({{ cat.repos | size }})</strong></summary>
{% else %}
<h2 id="{{ cat.title | slugify }}">{{ cat.title }}</h2>
{% endif %}
{% if cat.links.size > 0 %}
<p>{% for link in cat.links %}<a href="{{ link.url }}">{{ link.title }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}</p>
{% endif %}
<table class="sw-table">
  <thead>
    <tr>
      <th>Repository</th>
      <th class="num">Stars</th>
      <th class="num">Issues</th>
      <th class="num">PRs</th>
      <th class="num">Last commit</th>
      <th class="num">Commits</th>
      <th>Release</th>
    </tr>
  </thead>
  <tbody>
  {% for r in cat.repos %}
    <tr>
      <td>
        <a href="{{ r.url }}"><strong>{{ r.name }}</strong></a>
        {% if r.homepage != "" %}(<a href="{{ r.homepage }}">docs</a>){% endif %}
        <span class="sw-desc">{{ r.description }}{% if r.language != "" %} [{{ r.language }}]{% endif %}</span>
      </td>
      <td class="num">{{ r.stars }}</td>
      <td class="num"><a href="{{ r.url }}/issues">{{ r.open_issues }}</a></td>
      <td class="num"><a href="{{ r.url }}/pulls">{{ r.open_prs }}</a></td>
      <td class="num">{{ r.last_commit }}</td>
      <td class="num{% if r.commits_recent == 0 %} sw-idle{% endif %}">{{ r.commits_recent }}</td>
      <td class="sw-release">{% if r.release != "" %}<a href="{{ r.release_url }}">{{ r.release }}</a><br><span class="sw-desc">{{ r.release_date }}</span>{% endif %}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>
{% if cat.title == "Other repositories" %}
</details>
{% endif %}
{% endfor %}

## Matrix communication and encryption guides

* [Koushi](https://github.com/shinaoka/koushi-matrix) — an experimental Matrix client for macOS (currently dogfooding; Windows support is not yet tested)
* **Windows:** use [Element Desktop](https://element.io/en/download). Element X is not available for Windows; verify the Element Desktop session and enable Secure Backup.
* **New Matrix users:** [日本語の暗号化設定チェックリスト](/blog/matrix-encryption-setup-checklist-ja/) / [English setup checklist](/blog/matrix-encryption-setup-checklist/)
* **Existing Matrix users:** [日本語の安全確認・回復チェックリスト](/blog/matrix-encryption-safety-recovery-checklist-ja/) / [English safety and recovery checklist](/blog/matrix-encryption-safety-recovery-checklist/)

The two guides cover recovery keys, Secure Backup, device verification, and recovery procedures for encrypted Matrix messages.
