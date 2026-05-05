---
name: linkedin-post-adapter
description: Adapts an existing news post (Obsidian file) into a LinkedIn post following the LinkedIn Post Guidebook 2026. Use when the user asks to adapt, convert, reformat, or rewrite a news article or Obsidian note as a LinkedIn post.
---

# LinkedIn Post Adapter

Takes a news post (Obsidian file) provided by the user and transforms it into a high-converting LinkedIn post following the LinkedIn Post Guidebook.

## Workflow

```
Step 1: Read the source file + Company Summary + LinkedIn Guidebook
Step 2: Write the LinkedIn post (confirm language with user)
Step 3: On approval → save to Obsidian + update posts-history
```

---

## Step 1 — Read Source Material

Run all three reads in parallel:

**1a. Source news post**
The user will provide a file path or name. Use Glob if needed:
```
glob: **/*[keyword]*
```
Read the file and extract: core topic, key facts, data points, and main insight.

**1b. LinkedIn Post Guidebook**
Use Glob to find it:
```
glob: **/*LinkedIn Post Guidebook*
```
Read the file found.

**1c. Selling Post structure chapters**
Use Glob to find each:
```
glob: **/*Core Principles*
glob: **/*Post Structure*Hooks*
```
Read both files found.

**1d. Company Summary (for Solbeg context)**
Use Glob to find it:
```
glob: **/*Company Summary*
```
Read the file found. Extract: relevant competency, specific proof points, differentiators tied to the news topic.

**Ask for post language before writing:**
> "What language should the post be written in? (English / Russian / other)"

Wait for the answer, then proceed.

---

## Step 2 — Write the LinkedIn Post

### Structure (mandatory)
```
[HOOK] → [VALUE / BODY] → [BRIDGE] → [CTA]
```

### HOOK — first 210 characters
- Must stop the scroll before "See more"
- Lead with: a surprising stat from the news, a bold claim, or an open loop
- Never start with "Excited to share…" or "We are happy to announce…"
- Choose one formula:
  - **Bold Claim:** "Most [profession] get [topic] wrong. Here's what the data shows."
  - **Data Hook:** "[Specific number] — here's what this means for your team."
  - **Open Loop:** "We tested [X]. The result surprised us."

### BODY
- Short paragraphs: 1–3 lines, blank line between each
- 3–5 key points drawn from the source news
- Use the news data concretely — no vague generalities
- Write as practitioners sharing real observations, not a marketing department
- Use "we", "our team", "we've seen" — not "Solbeg offers"

### BRIDGE (optional but preferred)
- Weave in a Solbeg proof point naturally
- Pattern: "We recently worked with a client who faced exactly this…"
- Use only real proof points from the Company Summary — never fabricate

### CTA — last 2–3 lines
- A specific question or invitation, not just "Follow us"
- Soft CTA examples:
  - "What's your take on this? Share below ↓"
  - "Are you seeing this shift in your projects? Let's discuss."
  - "DM us if you're navigating this — happy to share what's worked."

### Format Rules
- Length: 150–300 words (1,200–1,500 characters)
- Paragraphs ≤ 3 lines
- **Bold** sparingly — max once per paragraph
- 3–5 hashtags at the very end (never in the body)
- No links in the post body — instruct user to put them in the first comment

### Output Format
```
---
## LinkedIn Post Draft

[POST CONTENT HERE]

---
**Hashtags:** #[tag1] #[tag2] #[tag3] #[tag4]
**Source insight used:** [1-sentence summary of the key news fact]
**Solbeg angle:** [1-sentence on the proof point, or "none used"]
---
```

Ask: "Would you like to adjust anything (tone, length, CTA)? Or shall we save it?"

**Wait for user confirmation before saving.**

---

## Step 3 — Save to Obsidian

Trigger: user approves (says "save", "looks good", "yes", "ok", or similar).

### 3a. Save the post
Create a file at:
```
03-Resources/solbeg/Posts/[YYYY-MM-DD] - LinkedIn - [topic-slug].md
```
Where `[topic-slug]` = 3–5 words from the topic, lowercase, hyphen-separated.

File content:
```markdown
---
date: [YYYY-MM-DD]
source: [original file name]
platform: LinkedIn
language: [post language]
tags: [solbeg, linkedin, social-media, post]
---

# [Topic name]

[Full post content, exactly as written]

---

**Hashtags:** #[tag1] #[tag2] ...
**Source insight:** [1 sentence]
**Solbeg angle:** [1 sentence or "none"]
```

### 3b. Append to Posts History

Locate `posts-history.md` via glob `**/*posts-history*`. Append:
```
| [YYYY-MM-DD] | [Topic name] | LinkedIn | [post type/stage] |
```

### 3c. Confirm to the user
> "Post saved: `Posts/[filename]` — history updated."

---

## Quality Rules

- Hook must fit within 210 characters (≈ 1–2 short lines)
- Only use Solbeg proof points that exist in the Company Summary
- Every post must contain at least one concrete fact from the source news
- No links in the post body
- Hashtags: 3–5, specific > broad, placed at the very end

## Resources

All files are located via Glob search — no hardcoded paths:
- LinkedIn Post Guidebook → `glob: **/*LinkedIn Post Guidebook*`
- Selling Post Framework → `glob: **/*Post Structure*Hooks*`
- Company context → `glob: **/*Company Summary*`
- Posts history → `glob: **/*posts-history*`
