---
name: youtube-search
description: Search YouTube using yt-dlp and return structured results: title, views, author, duration, upload date, and URL. Use when the user asks to search YouTube, find videos, look up a YouTube channel, or discover content on YouTube.
---

# YouTube Search

Uses `yt-dlp` to query YouTube and return structured video metadata — no API key required.

## Prerequisites

`yt-dlp` must be installed:
```bash
pip install yt-dlp
# or
winget install yt-dlp
```

## Run a search

```bash
python scripts/search.py "QUERY" [--limit N]
```

- Default limit: **5** results.
- Increase with `--limit 10` (max 20 to stay fast).

## Output format

Each result is printed as a markdown table row:

| # | Title | Author | Duration | Views | Date | URL |
|---|-------|--------|----------|-------|------|-----|

Render the table in your response for readability.

## Direct yt-dlp command (fallback)

If the script is unavailable, run directly in Shell:

```bash
yt-dlp "ytsearch5:QUERY" \
  --print "%(title)s\t%(uploader)s\t%(duration_string)s\t%(view_count)s\t%(upload_date)s\t%(webpage_url)s" \
  --no-download --no-warnings
```

Replace `ytsearch5` with `ytsearchN` for N results.

## Additional resources

- For field reference and formatting details, see [reference.md](reference.md)
