---
name: medium-post-adapter
description: Adapts an existing news post (Obsidian file) into a full-length Medium article following the Medium Article Guidebook 2026. Use when the user asks to adapt, convert, expand, or rewrite a news article or Obsidian note as a Medium article or post.
---

# Medium Post Adapter

Takes a news post (Obsidian file) provided by the user and expands it into a publication-ready Medium article following the Medium Article Guidebook 2026.

## Workflow

```
Step 1: Read the source file + Company Summary + Medium Guidebook
Step 2: Write the Medium article (confirm language with user)
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
Read the file and extract: core topic, key facts, data points, main insight, and any examples or case details.

**1b. Medium Article Guidebook**
Use Glob to find it:
```
glob: **/*Medium Article Guidebook*
```
Read the file found.

**1c. Company Summary (for Solbeg context)**
Use Glob to find it:
```
glob: **/*Company Summary*
```
Read the file found. Extract: relevant competency or case study that supports the article's thesis.

**Ask for article language before writing:**
> "What language should the article be written in? (English / Russian / other)"

Wait for the answer, then proceed.

---

## Step 2 — Write the Medium Article

### Headline
Test 3 variations using these formulas:
- **Specific result + timeframe:** "How [X] Changed in [Timeframe] — And What It Means for Your Team"
- **Number + benefit:** "[N] Things the [News Topic] Reveals About [Relevant Problem]"
- **Counterintuitive take:** "Why [Common Assumption] Is Wrong — [News Topic] Proves It"

Choose the strongest. The headline must accurately reflect the content — no clickbait.

### Article Structure

**Opening (200–300 words)**
- Lines 1–3: a counterintuitive statement or surprising data point from the news — the hook
- Context: why this news matters to the reader right now
- Preview: what the article covers and what the reader will gain
- Optional: 1–2 sentences establishing authority (Solbeg's experience in this domain)

**Body (1,000–2,000 words)**
Follow this pattern for each section:
```
Insight → Evidence (from source news) → Implication for the reader
```
- 3–5 main sections with H2 headings
- New H2 every 300–500 words
- Paragraphs: 2–4 sentences maximum, blank line between each
- Every 3 paragraphs: one short sentence that creates curiosity ("micro-hook")
- Concrete examples and data — no generic statements
- Weave in Solbeg experience naturally where relevant:
  *"In our work with clients navigating this shift, we've found…"*
  Use only real proof points from the Company Summary.

**Conclusion (150–200 words)**
- Synthesize 2–3 key takeaways from the article
- Provide actionable next steps for the reader
- End with a thought-provoking question or prediction

### Format Rules
- Minimum length: 1,200 words (1,500–2,000 preferred for curation)
- H2 for main sections, H3 for subsections
- **Bold** for key phrases, used sparingly
- Block quotes for important insights
- Bullet/numbered lists for scannable content — avoid text walls
- No affiliate links in the first 3 paragraphs
- No self-promotion without value — the article must stand alone as useful content

### Tags (3–5)
Choose specific tags that accurately match the content. Do NOT pick broad tags for reach.
- Example: article about AI in healthcare → "Artificial Intelligence", "Healthcare Technology", "Digital Health" (not just "Technology")

### Output Format

```
---
## Medium Article Draft

**Headline:** [Chosen headline]

**Alternative headlines:**
- [Option 2]
- [Option 3]

---

[FULL ARTICLE CONTENT]

---

**Suggested tags:** [tag1], [tag2], [tag3], [tag4]
**Word count:** ~[N] words
**Core thesis:** [1-sentence summary]
**Solbeg angle used:** [1 sentence, or "none"]
---
```

Ask: "Would you like to adjust anything (headline, tone, length, conclusion)? Or shall we save it?"

**Wait for user confirmation before saving.**

---

## Step 3 — Save to Obsidian

Trigger: user approves (says "save", "looks good", "yes", "ok", or similar).

### 3a. Save the article
Create a file at:
```
03-Resources/solbeg/Posts/[YYYY-MM-DD] - Medium - [topic-slug].md
```
Where `[topic-slug]` = 3–5 words from the topic, lowercase, hyphen-separated.

File content:
```markdown
---
date: [YYYY-MM-DD]
source: [original file name]
platform: Medium
headline: [chosen headline]
language: [article language]
tags: [solbeg, medium, article, content]
medium-tags: [[tag1], [tag2], [tag3]]
---

# [Chosen headline]

[Full article content, exactly as written]

---

**Suggested Medium tags:** [tag1], [tag2], [tag3]
**Core thesis:** [1 sentence]
**Solbeg angle:** [1 sentence or "none"]
```

### 3b. Append to Posts History

Locate `posts-history.md` via glob `**/*posts-history*`. Append:
```
| [YYYY-MM-DD] | [Topic name] | Medium | [article type] |
```

### 3c. Confirm to the user
> "Article saved: `Posts/[filename]` — history updated."

---

## Quality Rules

- Minimum 1,200 words — articles under this threshold are rarely curated
- Opening hook must appear in the first 1–3 lines
- Every section must follow: Insight → Evidence → Implication
- 3–5 tags, specific not broad — mismatch leads to rejection
- No republishing content verbatim from other platforms
- Only use Solbeg proof points that exist in the Company Summary
- Conclusion must end with a question or prediction — not a generic summary

## Resources

All files are located via Glob search — no hardcoded paths:
- Medium Article Guidebook → `glob: **/*Medium Article Guidebook*`
- Company context → `glob: **/*Company Summary*`
- Selling Post principles → `glob: **/*Core Principles*`
- Posts history → `glob: **/*posts-history*`
