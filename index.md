---
layout: template
---

<ul class="list-unstyled index">
  {% for post in site.posts %}
  <li><span class="text-muted date">[{{ post.date | date_to_string }}]</span> <a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
