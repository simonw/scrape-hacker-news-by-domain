"""
Fetch the 30 most recent Hacker News submissions from a domain (including its
subdomains) using the Algolia HN Search API, matching the output that
news.ycombinator.com/from?site=DOMAIN would give.

Usage: python fetch.py simonwillison.net simonwillison-net.json
"""

import json
import sys
import time
import urllib.parse
import urllib.request

API = "https://hn.algolia.com/api/v1/search_by_date"


def fetch_hits(domain):
    url = API + "?" + urllib.parse.urlencode(
        {
            "query": domain,
            "restrictSearchableAttributes": "url",
            "tags": "story",
            "hitsPerPage": 100,
        }
    )
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                return json.load(response)["hits"]
        except Exception as ex:
            if attempt == 3:
                raise
            print(f"Attempt {attempt + 1} failed: {ex}", file=sys.stderr)
            time.sleep(10 * 2**attempt)


def matches_domain(url, domain):
    hostname = urllib.parse.urlparse(url or "").hostname or ""
    return hostname == domain or hostname.endswith("." + domain)


def fetch(domain, limit=30):
    hits = [h for h in fetch_hits(domain) if matches_domain(h.get("url"), domain)]
    hits.sort(key=lambda h: h["created_at_i"], reverse=True)
    return [
        {
            "id": h["objectID"],
            "title": h["title"],
            "url": h["url"],
            "dt": h["created_at"].rstrip("Z"),
            "points": h["points"],
            "submitter": h["author"],
            "commentsUrl": f"https://news.ycombinator.com/item?id={h['objectID']}",
            "numComments": h.get("num_comments") or 0,
        }
        for h in hits[:limit]
    ]


if __name__ == "__main__":
    domain, output = sys.argv[1:]
    items = fetch(domain)
    if not items:
        sys.exit(f"No items found for {domain}")
    with open(output, "w") as fp:
        fp.write(json.dumps(items, indent=4) + "\n")
