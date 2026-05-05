---
name: medium-news-search
description: Search Medium for trending articles and stories on topics relevant to the company's activities. Generates topic suggestions based on a Company Summary found in the Obsidian vault, then finds and presents the most interesting Medium articles after topic confirmation. Use when the user asks to find Medium articles, trending tech topics, industry stories, engineering insights, or Medium content ideas.
---

# Medium News Search

## Overview

This skill finds trending Medium content on topics relevant to the company. It works in two phases:

1. **Topic suggestion** — locate the Company Summary in the Obsidian vault, then propose relevant topics
2. **Article discovery** — search and present the most interesting Medium articles on the confirmed topic

---

## Phase 1: Generate Topic Suggestions

### Step 1: Locate the Company Summary

Do NOT use a hardcoded path. Discover the file dynamically:

1. **Find the Obsidian vault path** by reading the Obsidian app config:
   - Windows: `%APPDATA%\obsidian\obsidian.json`
   - macOS: `~/Library/Application Support/obsidian/obsidian.json`
   - Linux: `~/.config/obsidian/obsidian.json`

   This JSON file contains a `vaults` object with `path` fields listing all vault directories.

2. **Search for the Company Summary** using the Glob tool with the pattern `**/*Company Summary*` inside each vault directory. Pick the first match.

3. **Fallback:** If the Obsidian config is not found, use the Glob tool with pattern `**/*Company Summary*` starting from the workspace root.

4. Read the located file to extract company context.

### Step 2: Present Topic Suggestions

Based on company activities, present **10–15 topic suggestions** grouped by category:

```
## Medium News — Topic Suggestions

Based on [Company Name]'s activities, here are relevant topics to explore on Medium:

### [Category 1]
- [topic 1]
- [topic 2]

### [Category 2]
- [topic 3]
- [topic 4]

[...up to 5 categories...]

---
Which topic interests you? Pick one from the list or suggest your own.
```

Derive all topics from actual company competencies read from the file — do not use generic topics.

---

## Phase 2: Search Medium Articles

After the user confirms a topic:

**Step 1:** Run 2–3 web searches in parallel:

```
site:medium.com "[topic]" 2026
"[topic]" medium.com engineering
"[topic]" site:medium.com -inurl:"/tag/"
```

Also try publication-specific searches:

```
site:medium.com/better-programming "[topic]"
site:levelup.gitconnected.com "[topic]"
site:medium.com/towards-data-science "[topic]"
```

**Step 2:** Prioritize articles with strong signals — claps, responses, featured in major publications (Better Programming, The Startup, Level Up Coding, Towards Data Science) or written by engineers from recognized companies.

**Step 3:** Present findings:

```
## Medium: [Topic Name]

### Top Articles

**1. [Article Title]**
- **Author:** [Name, Title / Company if known]
- **Publication:** [Medium publication or "Personal blog"]
- **Why it's interesting:** [1–2 sentences on the key insight or takeaway]
- **Link:** [URL]

[...repeat for 5–8 articles...]

---

### Key Themes in This Topic
- [Theme 1 — what practitioners are discussing most]
- [Theme 2]
- [Theme 3]

### Content Angle for [Company Name]
[1–2 sentences: how the company's experience connects to this topic — potential post angle, anchored to real proof points from the Company Summary]
```

---

## Quality Guidelines

- Prefer articles from the **last 60–120 days** — add `after:2026-01-01` to queries if needed
- Prioritize **engineers and practitioners** over generic bloggers
- Include a mix of **technical deep-dives, case studies, and opinion pieces**
- "Content Angle" must reference real proof points from the Company Summary, not generic statements
- If results are thin, broaden the query or suggest a related sub-topic

