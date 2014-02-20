---
layout: template
title: Blog
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
