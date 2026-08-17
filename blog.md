---
title: Blog
permalink: /blog/
layout: single
author_profile: false
classes: wide
---

<div class="notice--primary" markdown="1">
**Lecture notes**

[Julia Spring School 2026](/julia_spring_school_2026/) is available as a standalone lecture-note page.
</div>

<div class="notice--warning" markdown="1">
**Matrix encryption guides**

- New users: [日本語](/blog/matrix-encryption-setup-checklist-ja/) · [English](/blog/matrix-encryption-setup-checklist/)
- Existing users and recovery: [日本語](/blog/matrix-encryption-safety-recovery-checklist-ja/) · [English](/blog/matrix-encryption-safety-recovery-checklist/)

These checklists explain recovery keys, Secure Backup, device verification, and safe recovery without discarding the only remaining copy of encryption keys.
</div>

{% assign posts = site.blog | sort: "date" | reverse %}
{% for post in posts %}
<div class="list__item">
  <article class="archive__item">
    <h2 class="archive__item-title">
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </h2>
    <p class="page__meta">
      {{ post.date | date: "%Y-%m-%d" }}{% if post.lang %} · {{ post.lang }}{% endif %}
    </p>
    <p class="archive__item-excerpt">
      {{ post.excerpt | default: post.content | strip_html | strip_newlines | replace: "  ", " " | truncate: 220 }}
    </p>
    <p>
      <a href="{{ post.url | relative_url }}">Read on this site</a>
      {% if post.original_url %}
        · <a href="{{ post.original_url }}">Original on Zenn</a>
      {% endif %}
    </p>
  </article>
</div>
{% endfor %}
