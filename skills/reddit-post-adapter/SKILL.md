---
name: reddit-post-adapter
description: Adapts an existing news post (Obsidian file) into a Reddit post following the Reddit Post Guidebook. Use when the user asks to adapt, convert, reformat, or rewrite a news article or Obsidian note as a Reddit post.
---

# Reddit Post Adapter

Takes a news post (Obsidian file) provided by the user and transforms it into a community-ready Reddit post following the Reddit Post Guidebook.

## Workflow

```
Step 1: Read the source file + Company Summary + Reddit Guidebook
Step 2: Write the Reddit post (confirm language with user)
Step 3: On approval → save to Obsidian + update posts-history
```

---

## Step 1 — Read Source Material

Run all reads in parallel:

**1a. Source news post**
The user will provide a file path or name. Use Glob if needed:

```
glob: **/*[keyword]*
```

Read the file and extract: core topic, key facts, data points, main insight, and any concrete examples or numbers.

**1b. Reddit Post Guidebook**
Use Glob to find it:

```
glob: **/*Reddit Post Guidebook*
```

Read the file found.

**1c. Company Summary (for Solbeg context)**
Use Glob to find it:

```
glob: **/*Company Summary*
```

Read the file found. Extract: relevant experience or case that can be presented as a genuine practitioner's perspective — not a marketing pitch.

**Ask for post language before writing:**

> "What language should the post be written in? (English / Russian / other)"

Also ask:

> "Do you have a target subreddit in mind? (e.g. r/programming, r/SaaS, r/Entrepreneur) — or should I suggest the best fit?"

Wait for the answers, then proceed.

---

## Step 2 — Write the Reddit Post

### Subreddit Selection

If the user didn't specify a subreddit, suggest 2–3 options based on the topic:

| Topic type             | Suggested subreddits                          |
| ---------------------- | --------------------------------------------- |
| Tech / Engineering     | r/programming, r/webdev, r/devops             |
| AI / ML                | r/MachineLearning, r/artificial, r/LocalLLaMA |
| Business / SaaS        | r/SaaS, r/Entrepreneur, r/startups            |
| Software development   | r/softwaredevelopment, r/ExperiencedDevs      |
| Cloud / Infrastructure | r/devops, r/sysadmin, r/aws                   |

Remind the user: read the subreddit rules before posting, and check karma requirements.

### Post Type

For professional and technical topics — always default to **Text (Self)** post. Note this in the output.

### Title

Write 3 title variants using different formulas:

- `I/We did X. Here is what happened.` — personal experience with specifics
- `[N] things we learned from [topic]` — non-obvious insights only
- `Why [common belief] is wrong — [data or example]` — contrarian angle

Rules:

- Specific > generic — include real numbers from the source news
- First 80 characters must contain the main point
- No clickbait, no ALL CAPS, no buzzwords ("game-changer", "revolutionary")
- Cannot be edited after publishing — choose carefully
- Optimal length: 80–150 characters

Choose the strongest title and mark it as recommended.

### Core Message

Write one sentence that captures the thesis:

> _"After reading this post, the reader should walk away with one clear insight they can retell to a colleague."_

One post — one idea.

### Body Structure

**Opening (first 2 sentences)**
Choose one:

- **Lead with the result:** "We went from X to Y in Z weeks using [approach]."
- **Acknowledge a shared frustration:** "Every article says [X]. Nobody tells you what that actually means."
- **Contrarian claim:** "Most people assume [X]. We assumed the same — and were wrong."

**Body**

- Paragraphs of 2–3 sentences, blank line between each
- 3–5 key points from the source news — concrete, data-backed, not generic
- Write as a practitioner: use "we", "our team", "in our experience"
- Weave in Solbeg experience naturally only if it adds value and reads as a genuine contribution, not a promo — use only real proof points from the Company Summary
- Numbered lists for step-by-step content; bullet lists for parallel items
- **Bold** for the single most important takeaway per section — use sparingly
- For posts > 400 words: use `##` section headers

**Closing / CTA**

- Ask one specific, open question: `"How are you handling this in your projects?"`
- Or invite discussion: `"Happy to answer questions in the comments"`
- Never: "Follow us", "Check out our site", "Visit solbeg.com"

### Format Rules

- Length: 200–600 words (Text posts perform best in this range)
- Paragraphs ≤ 3 sentences with blank lines between them
- No links to own resources without context
- No hashtags (Reddit does not use them)
- Flair: suggest the most appropriate flair based on the subreddit

### Output Format

```
---
## Reddit Post Draft

**Recommended subreddit:** r/[subreddit]
**Post type:** Text (Self)
**Suggested flair:** [flair name or "check subreddit rules"]
**Recommended posting time:** Tue–Thu, 8:00 AM–12:00 PM EST

---

**Title options:**
1. ✅ [Recommended title]
2. [Alternative 1]
3. [Alternative 2]

---

**Core message:** [1-sentence thesis]

---

[FULL POST BODY]

---

**Solbeg angle:** [1-sentence on the proof point used, or "none — kept fully practitioner-neutral"]
---
```

Ask: "Would you like to adjust anything (title, subreddit, tone, CTA)? Or shall we save it?"

**Wait for user confirmation before saving.**

---

## Step 3 — Save to Obsidian

Trigger: user approves (says "save", "looks good", "yes", "ok", or similar).

### 3a. Save the post

Create a file at:

```
03-Resources/solbeg/Posts/[YYYY-MM-DD] - Reddit - [topic-slug].md
```

Where `[topic-slug]` = 3–5 words from the topic, lowercase, hyphen-separated.

File content:

```markdown
---
date: [YYYY-MM-DD]
source: [original file name]
platform: Reddit
subreddit: r/[subreddit]
language: [post language]
tags: [solbeg, reddit, social-media, post]
---

# [Chosen title]

[Full post body, exactly as written]

---

**Subreddit:** r/[subreddit]
**Suggested flair:** [flair]
**Core message:** [1 sentence]
**Solbeg angle:** [1 sentence or "none"]
```

### 3b. Append to Posts History

Locate `posts-history.md` via glob `**/*posts-history*`. Append:

```
| [YYYY-MM-DD] | [Topic name] | Reddit (r/[subreddit]) | [post type] |
```

### 3c. Confirm to the user

> "Post saved: `Posts/[filename]` — history updated."

---

## Quality Rules

- Title must be specific, non-clickbait, and contain the main point in the first 80 characters
- Opening must hook the reader in the first 2 sentences
- One post — one idea: if the source has multiple angles, pick the strongest one
- No links to own resources unless they add direct value and are not the focus of the post
- No hashtags
- Solbeg context must read as genuine practitioner experience — never as promotion
- Only use proof points that exist in the Company Summary
- Every post must include at least one concrete fact or number from the source news
- Remind the user to reply to every comment within the first 1–2 hours after publishing

## Resources

All files are located via Glob search — no hardcoded paths:

- Reddit Post Guidebook → `glob: **/*Reddit Post Guidebook*`
- Company context → `glob: **/*Company Summary*`
- Posts history → `glob: **/*posts-history*`

