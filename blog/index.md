---
layout: template
title: Blog
---

#### Lytro
{% for post in site.categories.lytro %}
- [{{ post.title }}]({{ post.url }}) [{{ post.date | date_to_string }}]
{% endfor %}

#### Linux
{% for post in site.categories.linux %}
- [{{ post.title }}]({{ post.url }}) [{{ post.date | date_to_string }}]
{% endfor %}
