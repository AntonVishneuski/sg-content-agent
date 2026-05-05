---
name: reddit-news-search
description: Search Reddit for trending discussions and posts on topics relevant to the company's activities. Generates topic suggestions based on a Company Summary found in the Obsidian vault, then finds and presents the most interesting Reddit threads after topic confirmation. Use when the user asks to find Reddit discussions, trending tech topics, community conversations, subreddit posts, or Reddit content ideas.
---

# Reddit News Search

Works in two phases:

1. **Topic suggestion** — find company context, propose relevant search topics
2. **Content discovery** — search Reddit and present the most interesting threads on the confirmed topic

---

## Phase 1: Find Company Context & Suggest Topics

### Step 1 — Locate Company Summary in the Vault

Do NOT use a hardcoded path. Discover the file dynamically:

1. **Find the Obsidian vault path** by reading the Obsidian app config:
   - Windows: `%APPDATA%\obsidian\obsidian.json`
   - macOS: `~/Library/Application Support/obsidian/obsidian.json`
   - Linux: `~/.config/obsidian/obsidian.json`

   This JSON file contains a `vaults` object with `path` fields listing all vault directories.

2. **Search for the Company Summary** using the Glob tool with the pattern `**/*Company Summary*` inside each vault directory. Pick the first match.

3. **Fallback:** If the Obsidian config is not found, use the Glob tool with patterns in parallel:
   ```
   glob: **/*ompany*ummary*
   glob: **/*ompany*rofile*
   glob: **/*ompany*verview*
   ```

4. Read the located file and extract:
   - Core services and products
   - Industries served
   - Key technologies and methodologies
   - Proven results and differentiators

### Step 2 — Present Topic Suggestions

Generate **10–15 topics** derived strictly from what you read. Group by category. Use this template:

```
## Reddit News — Topic Suggestions

Based on [Company Name]'s activities, here are relevant topics to explore on Reddit:

### [Category 1]
- [topic]
- [topic]

### [Category 2]
- [topic]
- [topic]

[...up to 5 categories...]

---
Which topic interests you? Pick one from the list or suggest your own.
```

Categories must reflect actual company competencies read from the file — do not use generic placeholder categories.

---

## Phase 2: Search Reddit Content

After the user confirms a topic, run 2–3 web searches **in parallel**:

```
site:reddit.com "[topic]"
"[topic]" reddit discussion [current year]
site:reddit.com "[topic]" comments:100
```

Also try subreddit-targeted searches based on the topic type:

| Topic type | Target subreddit searches |
|---|---|
| Tech / Engineering | `site:reddit.com/r/programming "[topic]"` |
| AI / ML | `site:reddit.com/r/MachineLearning "[topic]"` |
| Business / SaaS | `site:reddit.com/r/SaaS "[topic]"` or `r/startups` |
| Cloud / DevOps | `site:reddit.com/r/devops "[topic]"` |
| Software dev | `site:reddit.com/r/ExperiencedDevs "[topic]"` |

Scan results for:

- High comment counts (100+ indicates active debate)
- High upvote/engagement ratios
- Threads from the last 30–90 days (add `after:YYYY-MM-DD` if results are stale)
- Posts by domain experts or practitioners with detailed, substantive comments
- Threads where top comments add new insight beyond the original post

Present findings using this template:

```
## Reddit: [Topic Name]

### Top Threads & Discussions

**1. [Thread title]**
- **Subreddit:** r/[subreddit]
- **Engagement:** [upvotes] upvotes · [N] comments
- **Why it's interesting:** [1–2 sentences — key insight, debate angle, or community consensus]
- **Link:** [URL]

**2. ...**

[5–8 threads total]

---

### Key Themes in This Topic
- [What practitioners are debating most]
- [Second theme — pain points, controversies, lessons]
- [Third theme]

### Subreddits Most Active on This Topic
- r/[subreddit1] — [1-sentence on tone and focus]
- r/[subreddit2] — [1-sentence]

### Content Angle for [Company Name]
[1–2 sentences: how the company's experience connects to this discussion — a potential post angle, anchored to real proof points from the Company Summary]
```

The "Content Angle" section must reference actual facts from the Company Summary — never generic statements.

---

## Quality Rules

- Prefer threads from the **last 60–90 days** — add `after:YYYY-01-01` to queries if needed
- Prioritize threads with **substantive top comments** — not just upvotes on the original post
- Include a mix of: **technical debates, experience reports, questions with expert answers, and case discussions**
- "Content Angle" must be anchored to real proof points — not generic company claims
- If search results are thin, broaden the query, try adjacent subreddits, or propose a related sub-topic
- Never fabricate thread URLs, upvote counts, or author names — only include real results
- If the vault has no company file and the user doesn't provide one, skip Phase 1 and ask for a brief company description before generating topics
