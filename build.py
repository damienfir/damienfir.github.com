from glob import glob
import json
import os
import os.path
import re
import subprocess
from datetime import datetime


def index_html(pages):
    s = """
    <!doctype html>
    <html lang="en">
      <head>
    <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="/bootstrap-5.0.0-beta1-dist/css/bootstrap.min.css">

        <title>Damien Firmenich</title>
      </head>
      <body>
        <div class="container">
        <ul class="list-unstyled">
        {posts}
        </ul>

        <p><small>Last updated: {last_updated:%Y-%m-%d}</small></p>

        </div>
      </body>
    </html>
    """
    sorted_pages = sorted(pages, key=lambda x: x["date"], reverse=True)
    links = [
        "<li><a href='{folder}'>{title}</a> <small class='text-muted'>[{date}]</small></li>".format(**page) for page in sorted_pages
    ]
    now = datetime.now()
    s = s.format(posts="".join(links), last_updated=now)
    return s


def post_html(post):
    s = """
    <!doctype html>
    <html>
    <head>
    <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="/bootstrap-5.0.0-beta1-dist/css/bootstrap.min.css">

        <title>{title}</title>
    </head>
    <body>
     {content}
    </body>
    </html>
    """
    return s.format(**post)


posts = glob("_posts/*")

os.makedirs("posts", exist_ok=True)

pages_list = []

for post in posts:
    date, name = os.path.basename(post).split("_")
    title = json.load(open(post + "/meta.json"))["title"]
    content = open(post + "/post.html").read()
    folder = "posts/" + name

    d = {
        "title": title,
        "content": content,
        "folder": folder,
        "date": date,
        "name": name
    }

    os.makedirs(folder, exist_ok=True)
    with open(folder + "/index.html", 'w') as fp:
        fp.write(post_html(d))

    # copy other files
    subprocess.run(f"cp -r {post}/* {folder}/", check=True, shell=True)

    pages_list.append(d)

with open("index.html", 'w') as fp:
    fp.write(index_html(pages_list))
