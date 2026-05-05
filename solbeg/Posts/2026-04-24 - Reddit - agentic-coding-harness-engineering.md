---
date: 2026-04-24
source: 2026-04-24 - agentic-coding-harness-engineering.md
platform: Reddit
subreddit: r/ExperiencedDevs
language: English
tags: [solbeg, reddit, social-media, post]
---

# We added AI coding agents to our CI/CD pipeline. 87% faster PRs. Here's what nobody tells you.

Every article about agentic coding tools talks about adoption metrics. None of them talk about what happens at 2am when the agent's PR looks clean, passes CI, and is quietly wrong.

We've been integrating AI coding agents into our delivery workflow — the kind that read your full repo, decompose tasks, write tests, fix failures, and submit pull requests without anyone at the keyboard.

The numbers are real. PR cycle times compressed by up to 87%. Boilerplate work cut in half. Features moving from spec to review in under 30 minutes.

But Thoughtworks flagged something important in their April 2026 Technology Radar: the industry isn't hitting an adoption wall. It's hitting a **reliability wall**. They have a name for the emerging discipline around it: "harness engineering."

**What harness engineering actually means in practice:**

- Measure iteration cycles per task — not just code throughput. An agent that writes 200 lines in 3 minutes and requires 6 revision cycles is not faster than a developer who writes 50 clean lines.
- Track post-merge rework and failed builds — not PR volume. Volume is the wrong signal entirely.
- Define hard scope boundaries for what agents can and cannot touch. Agents that drift outside their intended scope create architectural debt fast.
- Build deliberate human review checkpoints. The agent handles the mechanical work; a human signs off on the judgment calls.

Here's the pattern we keep seeing: **the teams that ship reliably with AI agents are the ones that already had the engineering fundamentals in place.** CI/CD pipelines, automated test coverage, clear module boundaries — these aren't prerequisites for AI adoption, they're what make AI adoption trustworthy.

We cut QA time by 70% through automated testing before we added agents into the mix. That foundation is what made the agent's output auditable.

If you're running agentic tools on a real production codebase — how are you handling scope boundaries and review checkpoints? Genuinely curious what's working for others.

---

**Subreddit:** r/ExperiencedDevs
**Suggested flair:** Discussion
**Core message:** Agentic coding tools work reliably only when the engineering fundamentals — CI/CD, automated testing, clear architectural scope — were already in place before you introduced the agents.
**Solbeg angle:** 70% QA time reduction through automated testing as the engineering foundation that makes agentic AI output trustworthy — presented as genuine practitioner experience.
