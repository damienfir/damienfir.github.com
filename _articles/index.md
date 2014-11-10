---
layout: template
title: Blog
date: 2014-11-10
---

#### Light field imaging
{% for post in site.categories.light-field %}
[{{ post.title }}]({{ post.url }}) [{{ post.date | date_to_string }}]
{% endfor %}

---

#### Linux
{% for post in site.categories.linux %}
[{{ post.title }}]({{ post.url }}) [{{ post.date | date_to_string }}]
{% endfor %}
