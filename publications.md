---
layout: template
title: Publications
---

{% for post in site.categories.publications %}

### {{ post.title }}

{{ post.content }}

--- 

{% endfor %}
