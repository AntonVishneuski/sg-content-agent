#!/usr/bin/env python3
"""YouTube search via yt-dlp. Returns structured video metadata."""

import argparse
import subprocess
import sys
from datetime import datetime


FIELDS = "%(title)s\t%(uploader)s\t%(duration_string)s\t%(view_count)s\t%(upload_date)s\t%(webpage_url)s"


def fmt_views(raw: str) -> str:
    try:
        n = int(raw)
        if n >= 1_000_000:
            return f"{n / 1_000_000:.1f}M"
        if n >= 1_000:
            return f"{n / 1_000:.0f}K"
        return str(n)
    except ValueError:
        return raw


def fmt_date(raw: str) -> str:
    try:
        return datetime.strptime(raw, "%Y%m%d").strftime("%Y-%m-%d")
    except ValueError:
        return raw


def search(query: str, limit: int) -> None:
    cmd = [
        "yt-dlp",
        f"ytsearch{limit}:{query}",
        "--print", FIELDS,
        "--no-download",
        "--no-warnings",
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    except FileNotFoundError:
        print("Error: yt-dlp not found. Install with: pip install yt-dlp", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.strip()}", file=sys.stderr)
        sys.exit(1)

    lines = [l for l in result.stdout.strip().splitlines() if l]
    if not lines:
        print("No results found.")
        return

    header = "| # | Title | Author | Duration | Views | Date | URL |"
    sep    = "|---|-------|--------|----------|-------|------|-----|"
    print(header)
    print(sep)

    for i, line in enumerate(lines, 1):
        parts = line.split("\t")
        if len(parts) < 6:
            continue
        title, author, duration, views, date, url = parts[:6]
        title_link = f"[{title}]({url})"
        print(f"| {i} | {title_link} | {author} | {duration} | {fmt_views(views)} | {fmt_date(date)} | {url} |")


def main() -> None:
    parser = argparse.ArgumentParser(description="Search YouTube via yt-dlp")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--limit", type=int, default=5, help="Number of results (default: 5, max: 20)")
    args = parser.parse_args()
    args.limit = min(max(args.limit, 1), 20)
    search(args.query, args.limit)


if __name__ == "__main__":
    main()
