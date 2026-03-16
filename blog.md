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
