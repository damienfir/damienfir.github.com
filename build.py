import os
from datetime import datetime, timezone
from markdown import markdown
from feedgen.feed import FeedGenerator

# Generate list of posts on main page (with date and title)
# - separate pages from blog posts

pages = os.listdir("pages_")
os.makedirs("pages", exist_ok=True)

with open("template.html") as fp:
    template = fp.read()

feed = FeedGenerator()
feed.title("Damien Firmenich")
feed.link(href="http://www.damienfirmenich.com", rel="alternate")
feed.description("desc")

for page in pages:
    path = os.path.join("pages_", page)
    print("processing", path)

    with open(path) as fp:
        content = fp.read().split("---")
    front_matter = content[1]
    main = content[2]

    meta = {}
    for line in front_matter.splitlines():
        if not line:
            continue
        key, val = line.split(":")
        key = key.strip()
        val = val.strip()
        if key == "date":
            val = datetime.strptime(val, "%Y-%m-%d")
            val = val.astimezone(timezone.utc)
        meta[key] = val

    html = markdown(main)
    templated = template.format(content=html, **meta)

    page_name = page.split(".")[0]
    out_path = os.path.join("pages", page_name + ".html")
    with open(out_path, 'w') as fp:
        fp.write(templated)

    entry = feed.add_entry()
    entry.title(meta['title'])
    entry.published(meta['date'])
    entry.author([{
        "name": "Damien Firmenich",
        "email": "fir.damien@gmail.com"
    }])
    url = "https://damienfir.github.io/pages/{}.html".format(page_name)
    entry.link(href=url)
    entry.id(url)
    entry.content(templated)

feed.rss_file("rss.xml", pretty=True)
