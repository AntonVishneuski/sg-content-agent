# YouTube Search — Field Reference

## yt-dlp metadata fields used

| Field | yt-dlp key | Notes |
|-------|-----------|-------|
| Title | `%(title)s` | Raw video title |
| Author | `%(uploader)s` | Channel name |
| Duration | `%(duration_string)s` | Formatted as `H:MM:SS` or `M:SS` |
| Views | `%(view_count)s` | Integer, formatted to K/M by script |
| Date | `%(upload_date)s` | Raw: `YYYYMMDD`, formatted to `YYYY-MM-DD` |
| URL | `%(webpage_url)s` | Full `https://www.youtube.com/watch?v=…` |

## Increasing result count

`ytsearchN:QUERY` where N = number of results. yt-dlp fetches results in batches, so large N (>20) slows down significantly.

## Filtering by duration or date

Add `--match-filter` to the yt-dlp command:
```bash
# Videos shorter than 10 minutes
yt-dlp "ytsearch10:QUERY" --match-filter "duration < 600" ...

# Videos uploaded after 2024
yt-dlp "ytsearch10:QUERY" --match-filter "upload_date > 20240101" ...
```

## Sorting

yt-dlp returns results in YouTube's default search order. To sort by a field (e.g. view count), pipe through sort in the script or post-process the output.
