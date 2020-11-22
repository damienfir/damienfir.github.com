---
layout: template
title: Projects
---

<ul class="list-unstyled">
{% for post in site.categories.project %}
<li><a href="{{post.url}}">{{post.title}}</a> [{{post.date | date_to_string}}]</li>
{% endfor %}
</ul>
