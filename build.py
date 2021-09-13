import json
import os.path
import subprocess
from datetime import datetime
from feedgen.feed import FeedGenerator

build_folder = "build"
last_update = datetime.now().strftime("%Y-%m-%d")
fg = FeedGenerator()
fg.title("Damien Firmenich")
fg.link( href='http://example.com', rel='alternate' )
fg.description("asdfsa")

with open("template.html") as fp:
    template = fp.read()

for post_name in os.listdir("pages") + [""]:
    post_folder = os.path.join("pages", post_name)
    if not os.path.isdir(post_folder):
        continue

    with open(os.path.join(post_folder, "meta.json")) as fp:
        meta = json.load(fp)

    content = subprocess.check_output(
        ["pandoc", os.path.join(post_folder, "index.md")]).decode("utf-8")

    out_folder = os.path.join(build_folder, post_name)
    os.makedirs(out_folder, exist_ok=True)

    templated = template.format(content=content, last_update=last_update, **meta)
    with open(os.path.join(out_folder, "index.html"), 'w') as fp:
        fp.write(templated)
    
    fe = fg.add_entry()
    fe.title(post_name)
    fe.description("test")



fg.rss_file(os.path.join(build_folder, "rss.xml"), pretty=True)
