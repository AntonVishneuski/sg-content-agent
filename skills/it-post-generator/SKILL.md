---
name: it-post-generator
description: Generates personalized IT-industry social media posts for Solbeg by researching current trends across web, YouTube, LinkedIn, Medium, and Reddit — then writing high-converting content following the Selling Post Guidebook framework. Use when the user asks to write a social media post, create IT content, find tech topics for a post, generate LinkedIn/Facebook posts about technology, or create company posts about IT trends.
---

# IT Post Generator

Researches current IT trends, confirms topics with the user, then writes a personalized selling post for Solbeg following the Selling Post Guidebook framework.

## Workflow Overview

```
Step 0: Analyze posts-history → avoid repeating recent topics
Step 1: Research IT news (web + YouTube + LinkedIn + Medium + Reddit) in parallel
Step 2: Present topic list → wait for user selection
Step 3: Write the post using Selling Post Guidebook structure
Step 4: On user approval → save post as Obsidian note + append to posts-history
Step 5: Search for platform adapters → offer to adapt for specific social networks
```

---

## Step 0 — Analyze Posts History

Locate the posts-history file in the Obsidian vault:

```
glob pattern: **/*posts-history*
```

If found, read it and extract the **last 30 days** of post topics. Keep this list in context to avoid repeating topics in Step 1 and Step 3.

If not found, create it at:
```
03-Resources/solbeg/posts-history.md
```

with this initial structure:
```markdown
# Posts History

| Date | Topic | Platform | Post Type |
|------|-------|----------|-----------|
```

---

## Step 1 — Research IT News

Run **all five searches in parallel** and collect results:

### 1a. Web Search
Run 3 web searches simultaneously:
```
latest IT technology trends [current month year]
software development industry news [current month year]
enterprise digital transformation trends [current month year]
```

### 1b. YouTube Search
Find and follow the YouTube search skill dynamically:
```
glob pattern: **/youtube-search/SKILL.md
glob pattern: **/*youtube*search*SKILL*
```
Pick the first match and read it.

Search queries to run:
```
IT technology trends [current year]
software engineering news [current month year]
```
Use `--limit 8` for each query.

### 1c. LinkedIn Search
Find and follow the LinkedIn news search skill dynamically:
```
glob pattern: **/linkedin-news-search/SKILL.md
glob pattern: **/*linkedin*news*search*SKILL*
```
Pick the first match and read it.

Skip Phase 1 (topic suggestion) — go directly to Phase 2 with these queries:
```
site:linkedin.com/posts "software development" OR "AI" OR "cloud" OR "mobile"
"tech industry" linkedin trending [current year] CTO OR "VP Engineering"
```

### 1d. Medium Search
Find and follow the Medium news search skill dynamically:
```
glob pattern: **/medium-news-search/SKILL.md
glob pattern: **/*medium*news*search*SKILL*
```
Pick the first match and read it.

Skip Phase 1 — go directly to Phase 2 with these queries:
```
site:medium.com "software engineering" [current year]
site:medium.com/better-programming OR site:levelup.gitconnected.com [current year]
```

### 1e. Reddit Search
Find and follow the Reddit news search skill dynamically:
```
glob pattern: **/reddit-news-search/SKILL.md
glob pattern: **/*reddit*news*search*SKILL*
```
Pick the first match and read it.

Skip Phase 1 — go directly to Phase 2 with these queries:
```
site:reddit.com/r/programming "software engineering" OR "AI" [current year]
site:reddit.com/r/ExperiencedDevs OR site:reddit.com/r/MachineLearning [current year]
site:reddit.com/r/devops OR site:reddit.com/r/SaaS [current year]
```

---

## Step 2 — Present Topics for Confirmation

After collecting all research results, deduplicate and filter out topics from the last 30 days in posts-history. Then present a numbered list of **8–12 topics**:

```
## IT Post Topics — Pick Your Focus

Here are the most relevant and trending topics I found. Topics already covered recently have been excluded.

**Technology & Engineering**
1. [Topic] — [1-sentence why it's relevant now + source signal]
2. [Topic] — [...]

**AI & Data**
3. [Topic] — [...]
4. [Topic] — [...]

**Business & Digital Transformation**
5. [Topic] — [...]
6. [Topic] — [...]

[...continue with remaining categories...]

---
Which topic(s) interest you? Reply with numbers (e.g. "1, 3") or suggest your own angle.
```

**Wait for user response before proceeding.**

---

## Step 3 — Write the Post

### 3a. Read Company Context

Find the Company Summary dynamically using the Glob tool:
```
glob pattern: **/*Company Summary*
glob pattern: **/*ompany*ummary*
```
Pick the first match and read it.

Extract:
- Relevant competency that matches the chosen topic
- Specific proof points (client results, metrics, technologies)
- Differentiators that apply to this topic

### 3b. Read the Selling Post Guidebook

Find the guidebook chapters dynamically using the Glob tool:
```
glob pattern: **/*Selling Post Guidebook*/*01*Core*
glob pattern: **/*Selling Post Guidebook*/*02*Awareness*
glob pattern: **/*Selling Post Guidebook*/*04*Structure*
```
Run all three in parallel. Read each file found.

### 3b-1. Ask for Post Language

Before writing, ask the user:

> "What language should the post be written in? (English / Russian / other)"

Wait for the answer. Write the entire post — including hook, body, bridge, and CTA — in the language the user specifies.

### 3c. Determine Post Type

Based on the topic and context, choose the awareness stage:
- **Problem Aware (Stage 2)** — educational breakdown, "why this matters"
- **Solution Aware (Stage 3)** — comparison, "our approach vs. common approach"
- **Product Aware (Stage 4)** — case study / results story (default for Solbeg posts)

Default to **Stage 2–3** (educational + solution) unless user specifies otherwise.

### 3d. Write the Post

Follow the Selling Post Guidebook structure:
```
[HOOK] → [VALUE / BODY] → [BRIDGE] → [CTA]
```

**HOOK rules:**
- Lead with a story, surprising stat, or bold claim — never a generic opener
- Reference the specific technology or trend from the research
- Choose one of: Epiphany Story / Intent-Based / Bold Claim formula

**BODY rules:**
- 3–5 concrete points or a structured breakdown
- Include the actual trend/technology insight from research
- Write as if a group of senior engineers and business analysts are sharing observations — not as a marketing department
- Use first-person plural ("we", "our team", "we've seen")

**BRIDGE rules:**
- Weave in a Solbeg proof point naturally: *"We recently worked with a client who..."*
- Use real proof points from the Company Summary — never fabricate
- Connect the trend directly to what Solbeg can deliver

**CTA rules:**
- Match the stage: soft CTA for Stage 2–3 content
- Default soft CTA: "What's your experience with [topic]? Share below ↓" or "DM us if you're navigating this — happy to share what's worked for our clients."
- Avoid generic "Contact us" — make it conversational

**Tone:**
- Expert but accessible
- Sounds like practitioners sharing real observations, not a brand account
- No corporate fluff — specific, grounded, opinionated

**Length:**
- LinkedIn: 150–300 words (hook visible before "see more")
- The hook must be compelling in the first 2 lines

### 3e. Output Format

Present the post ready to copy-paste:

```
---
## 📝 Post Draft

[POST CONTENT HERE]

---
**Post type:** [Stage X — Educational/Solution/etc.]
**Awareness stage:** [Stage name]
**Key Solbeg angle:** [1 sentence on the proof point used]
**Suggested hashtags:** #[tag1] #[tag2] #[tag3] #[tag4] #[tag5]
---
```

Ask: "Would you like to adjust anything (tone, length, CTA)? Or shall we save it?"

---

## Step 4 — Save the Post and Update History

Do this **immediately after the user approves the post** (says "save", "ok", "yes", "looks good", or similar). Do not wait for a separate explicit save command.

### 4a. Save the Post as an Obsidian Note

Create a new file at:
```
03-Resources/solbeg/Posts/[YYYY-MM-DD] - [Topic slug].md
```

Where `[Topic slug]` is the topic name shortened to 3–5 words, spaces replaced with hyphens, lowercase.

File contents:
```markdown
---
date: [YYYY-MM-DD]
topic: [Full topic name]
platform: LinkedIn
stage: [Stage X — Educational/Solution/etc.]
language: [post language]
tags: [solbeg, social-media, post]
---

# [Topic name]

[Full post content, exactly as written]

---

**Hashtags:** #[tag1] #[tag2] ...
**Key Solbeg angle:** [1 sentence]
```

### 4b. Append to Posts History

Append a new row to `03-Resources/solbeg/posts-history.md`:

```markdown
| [YYYY-MM-DD] | [Topic name] | LinkedIn | [Stage X — type] |
```

### 4c. Confirm to the User

After both files are written, say:
> "Post saved to `Posts/[filename]` and added to posts history."

Then immediately proceed to **Step 5**.

---

## Step 5 — Offer Platform Adapters

### 5a. Find All Available Adapters

Run a Glob search **right now** (at the moment of offering, not earlier):

```
glob pattern: **/*Adapter*Skill*
glob pattern: **/*Skill*Adapter*
```

Search in the full Obsidian vault. Run both patterns in parallel.

For each found file, read its frontmatter and extract:
- `title` — display name of the adapter
- `skill-path` — path to the actual SKILL.md
- A 1-line description of what the adapter produces (from the file body — the `> ...` blockquote line)

### 5b. Present the Adapter Menu

If at least one adapter is found, present:

```
---
Would you like to adapt this post for a specific platform?

Available adapters:
1. [Adapter title] — [1-line description]
2. [Adapter title] — [1-line description]
[...all found adapters...]

Reply with the adapter number to adapt the post.
Or type "no" / "skip" to finish.
```

If no adapters are found, skip this step silently.

### 5c. Run the Selected Adapter

After the user picks an adapter:

1. Read the `skill-path` from the corresponding adapter file
2. Read the SKILL.md at that path
3. Follow the adapter skill's instructions, passing the **saved post file** (from Step 4a) as the source document
4. The adapter handles its own output saving and confirmation

---

## Quality Rules

- Never fabricate Solbeg proof points — use only what's in the Company Summary
- Never repeat a topic covered in the last 30 days (check posts-history)
- Every post must include: one trend insight from research + one Solbeg proof point
- Hook must appear in the first 1–2 lines (before LinkedIn's "see more" cutoff)
- Tone: practitioner-voice, not marketing-voice

## Additional Resources

- For Selling Post structure details — find via glob `**/*Selling Post Guidebook*/*.md`
- For Company proof points — find via glob `**/*Company Summary*`
