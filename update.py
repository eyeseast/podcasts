#!/usr/bin/env python3

import os
import pathlib
import sys
from urllib.request import urlretrieve

import feedparser
from slugify import Slugify

try:
    DOWNLOAD_LIMIT = int(os.environ.get("PODCAST_DOWNLOAD_LIMIT", 10))
except ValueError:
    DOWNLOAD_LIMIT = 10

slugify = Slugify(separator="_", to_lower=False)


def main(feeds_file: pathlib.Path, output_dir: pathlib.Path):
    with open(feeds_file) as f:
        for line in f:
            url = line.strip()
            if url:
                download_feed(line.strip(), output_dir)


def download_feed(url: str, output_dir: pathlib.Path):
    print(f"Loading feed: {url}")
    feed = feedparser.parse(url)
    print(f"Found podcast: {feed.feed.title}")

    for entry in feed.entries[:DOWNLOAD_LIMIT]:
        print(f"Downloading episode: {entry.title}")
        if not entry.get("enclosures"):
            print("No enclosures. Skipping.")

        # enclosures is a one-item list
        enclosure = entry.enclosures[0]
        kind = enclosure.get("type", "").split("/")[0]
        if kind != "audio":
            print(f"Unknown file type: {enclosure.get('type')}")
            continue

        save(enclosure.get("href", ""), entry.title, output_dir)


def save(href: str, title: str, output_dir: pathlib.Path):
    suffix = pathlib.Path(href).suffix
    path = output_dir / f"{slugify(title)}{suffix}"

    print(f"Saving URL: {href}")
    urlretrieve(href, path)
    print(f"Saved: {path}")


if __name__ == "__main__":
    feeds_file = pathlib.Path(sys.argv[1])
    output_dir = pathlib.Path(sys.argv[2])

    try:
        main(feeds_file, output_dir)
    except KeyboardInterrupt:
        print("Exiting.")
        sys.exit(0)
