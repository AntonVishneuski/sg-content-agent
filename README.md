# Solbeg Content Agent

AI agent for generating IT social media content for Solbeg (LinkedIn, Medium, Reddit).
Works in any folder via Claude Code — Obsidian is not required.

## What it does

- Finds current IT trends (Web, YouTube, LinkedIn, Medium, Reddit)
- Suggests topics, excluding ones already covered
- Writes posts in Solbeg's voice following the Selling Post Framework
- Adapts content for LinkedIn, Medium, and Reddit
- Saves post history

## Quick start

### 1. Create a folder for the agent

```bash
mkdir solbeg-content-agent && cd solbeg-content-agent
```

### 2. Open Claude Code in that folder

```bash
claude
```

### 3. Run one command

```
deploy agent https://gist.github.com/YOUR_USERNAME/GIST_ID
```

Claude will download the repository, set up the folder structure, install dependencies, and be ready to work.

### 4. Write a post

```
write a post
```

---

## Manual setup

```bash
git clone https://github.com/YOUR_USERNAME/solbeg-content-agent.git
cd solbeg-content-agent
```

Then open Claude Code and run `deploy agent`.

---

## Structure

```
.claude/skills/              ← Claude Code skills (created on deploy)
  it-post-generator/
  youtube-search/
  linkedin-news-search/
  linkedin-post-adapter/
  medium-news-search/
  medium-post-adapter/
  reddit-news-search/
  reddit-post-adapter/

03-Resources/                ← content (created on deploy)
  Selling Post Guidebook/    ← post writing framework
  solbeg/
    Solbeg - Company Summary.md
    posts-history.md
    Posts/

CLAUDE.md                    ← agent config
```

## Dependencies

- `yt-dlp` — for YouTube search (installed automatically, Python not required)

## Skills

| Skill | Description |
|-------|-------------|
| `it-post-generator` | Main orchestrator: trends → topic → post → save |
| `youtube-search` | YouTube search via yt-dlp |
| `linkedin-news-search` | Trending topics on LinkedIn |
| `linkedin-post-adapter` | Adapts post for LinkedIn |
| `medium-news-search` | Trending articles on Medium |
| `medium-post-adapter` | Adapts post for Medium |
| `reddit-news-search` | Trending discussions on Reddit |
| `reddit-post-adapter` | Adapts post for Reddit |
