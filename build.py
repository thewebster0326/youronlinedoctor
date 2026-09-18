#!/usr/bin/env python3
"""Build the static site.

    python build.py

Renders every page defined in builder/pages.py into the repository root,
then writes sitemap.xml and robots.txt. No dependencies.
"""

import io
import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from builder.config import BRAND
from builder.layout import render
from builder.pages import ALL_PAGES

ROOT = os.path.dirname(os.path.abspath(__file__))

# Pages excluded from sitemap.xml
NO_INDEX = {"404.html"}

PRIORITY = {
    "index.html": "1.0",
    "services.html": "0.9",
    "our-network.html": "0.9",
    "contact.html": "0.8",
}


def write(path, text):
    full = os.path.join(ROOT, path)
    directory = os.path.dirname(full)
    if directory and not os.path.isdir(directory):
        os.makedirs(directory)
    with io.open(full, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return len(text)


def build_sitemap(paths):
    today = date.isoformat(date.today())
    urls = []
    for path in paths:
        loc = BRAND["domain"] + "/" + ("" if path == "index.html" else path)
        urls.append(
            "  <url>\n"
            "    <loc>{loc}</loc>\n"
            "    <lastmod>{mod}</lastmod>\n"
            "    <priority>{pri}</priority>\n"
            "  </url>".format(loc=loc, mod=today, pri=PRIORITY.get(path, "0.7"))
        )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )


def build_robots():
    return (
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        "Sitemap: {}/sitemap.xml\n".format(BRAND["domain"])
    )


def main():
    built = []
    total = 0
    for page_fn in ALL_PAGES:
        page = page_fn()
        size = write(page["path"], render(page))
        total += size
        built.append(page["path"])
        print("  {:<34} {:>7,} bytes".format(page["path"], size))

    indexable = [p for p in built if p not in NO_INDEX]
    write("sitemap.xml", build_sitemap(indexable))
    write("robots.txt", build_robots())

    print("\n  {} pages, {:,} bytes of HTML".format(len(built), total))
    print("  sitemap.xml lists {} URLs".format(len(indexable)))


if __name__ == "__main__":
    main()
