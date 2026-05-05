---
name: linkedin-news-search
description: Search LinkedIn for trending news and posts on topics relevant to the company's activities. Automatically finds a Company Summary in the Obsidian vault, generates topic suggestions, then finds and presents the most interesting LinkedIn posts after topic confirmation. Use when the user asks to find LinkedIn news, trending topics, industry posts, or LinkedIn content ideas.
---

# LinkedIn News Search

Works in two phases:

1. **Topic suggestion** — find company context, propose relevant search topics
2. **Content discovery** — search LinkedIn and present the most interesting posts on the confirmed topic

---

## Phase 1: Find Company Context & Suggest Topics

### Step 1 — Locate Company Summary in the Vault

Use the Glob tool to search the workspace for company summary files:

```
glob pattern: **/*ompany*ummary*
glob pattern: **/*ompany*rofile*
glob pattern: **/*ompany*verview*
```

Run all three glob searches in parallel. If multiple files are found, present the list and ask the user which one to use. If none are found, ask the user to point to the file or provide the company description directly.

### Step 2 — Read the file

Read whichever file is confirmed (or found). Extract:

- What the company does (core services/products)
- Industries served
- Key technologies and methodologies
- Proven results and differentiators

### Step 3 — Present Topic Suggestions

Generate **10–15 topics** derived strictly from what you read. Group by category. Use this template:

```
## LinkedIn News — Topic Suggestions

### [Category 1]
- [topic]
- [topic]

### [Category 2]
- [topic]
- [topic]

[...repeat for all categories...]

---
Which topic interests you? Pick one or suggest your own.
```

Categories should reflect the actual company competencies — do not use generic placeholder categories.

---

## Phase 2: Search LinkedIn Content

After the user confirms a topic, run 2–3 web searches **in parallel**:

```
site:linkedin.com/posts "[topic]"
"[topic]" linkedin trending [current year]
"[topic]" site:linkedin.com CTO OR "VP Engineering" OR "tech lead"
```

Scan results for:

- Strong engagement signals (comments, reactions, reshares)
- Credible authors: CTOs, VPs, tech leads, recognized practitioners
- Posts from the last 30–90 days (add `after:YYYY-MM-DD` if results are stale)

Present findings using this template:

```
## LinkedIn: [Topic Name]

### Top Posts & Discussions

**1. [Post title or first line]**
- **Author:** [Name, Title @ Company]
- **Why it's interesting:** [1–2 sentences — key insight or angle]
- **Link:** [URL]

**2. ...**

[5–8 posts total]

---

### Key Themes
- [What's being discussed most]
- [Second theme]
- [Third theme]

### Content Angle for [Company Name]
[1–2 sentences connecting the trend to the company's real proof points from the Summary]
```

The "Content Angle" section must reference actual facts from the Company Summary — never generic statements.

---

## Quality Rules

- If search results are thin, broaden the query or propose a related topic
- Prefer original insights, case studies, and contrarian takes over listicles
- Never fabricate post URLs or author names — only include real results
- If the vault has no company file and the user doesn't provide one, skip Phase 1 and ask for a brief company description before generating topics

