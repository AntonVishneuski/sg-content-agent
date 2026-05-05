# CLAUDE.md — Obsidian Vault Context

This is an Obsidian vault organized with the **PARA method**.

## Structure


| Folder          | Purpose                                             |
| --------------- | --------------------------------------------------- |
| `00-Inbox/`     | Unprocessed captures, quick notes                   |
| `01-Projects/`  | Active projects with a defined outcome              |
| `02-Areas/`     | Ongoing responsibilities without a finish line      |
| `03-Resources/` | Reference material organized by topic               |
| `04-Archive/`   | Inactive projects, areas, and resources             |
| Sources/        | Literature notes, books, articles, podcasts, videos |
| `Topics/`       | Evergreen notes on concepts and ideas               |
| `Templates/`    | Note templates                                      |
|                 |                                                     |


## Conventions

- All notes are **Markdown** (`.md`).
- Internal links use **wiki-link syntax**: `[[Note Title]]`.
- Aliases: `[[Note Title|display text]]`.
- Tags use `#tag` inline or in YAML frontmatter.

## Where to Put New Notes

- **New concept or topic** → `Topics/`
- **New source** (book, article, video, paper) → `Sources/`
- **Quick capture** → `00-Inbox/` (to be processed later)
- **Active project** → `01-Projects/`

## Frontmatter Convention

```yaml
---
title: Note Title
date: YYYY-MM-DD
tags: [tag1, tag2]
source: "[[Source Note]]" # for derived notes
---
```

## Linking Style

- Prefer linking to atomic **Topics/** notes rather than repeating explanations.
- Always use the exact note filename in wiki-links to avoid broken links.
- Back-links are relied upon for navigation — link generously.

