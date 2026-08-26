# 01. Skills overview

- **Status:** Accepted
- **Date:** 2026-08-25
- **Type:** Reference
- **Audience:** Users and skill authors
- **Source files:** `skills/` (bundled categories), `optional-skills/`, `tools/skills_tool.py`
- **Related:** [User guide](../user-guide/01-overview.md), [agentskills.io open standard](https://agentskills.io)

## What skills are

A skill is procedural memory: a folder with a `SKILL.md` (frontmatter + method)
and optional reference files, invoked as `/<skill-name>` or selected
automatically by the agent. Hermes is compatible with the
[agentskills.io](https://agentskills.io) open standard.

## Where skills live

| Location | Contents |
|---|---|
| `skills/` (repo) | Bundled, curated skills in 15 categories: apple, autonomous-ai-agents, creative, devops, email, github, media, mlops, note-taking, productivity, research, smart-home, social-media, software-development (+ index cache). |
| `optional-skills/` (repo) | Opt-in heavyweight packs (e.g. creative-ideation methods library, audiocraft, kanban-video-orchestrator, concept-diagrams, hyperframes). |
| `~/.hermes/skills/` (user home) | User-created and imported skills; OpenClaw migration lands imports under `openclaw-imports/`. |
| Skills Hub ([agentskills.io](https://agentskills.io)) | Community distribution. |

## The learning loop

Hermes closes the loop around skills:

1. **Autonomous creation** — after complex tasks the agent can persist a new
   skill capturing the working procedure.
2. **Self-improvement** — during use, a skill's steps can be edited when the
   agent finds a better path.
3. **Persistence nudges** — the agent prompts itself to save recurring
   knowledge instead of losing it.

## Working with skills

```bash
/skills                 # browse installed skills (CLI & messaging)
/<skill-name>           # invoke directly
```

Skill execution goes through `tools/skills_tool.py`; remote/sandbox backends
use the same skill namespace so containerized runs see the user's skills.

## Writing one

Minimal viable structure:

```
my-skill/
  SKILL.md          # frontmatter (name, description) + instructions
  references/       # optional deep-dive docs loaded on demand
```

Keep `SKILL.md` self-sufficient for the common case; push detail into
reference files. See any bundled category for house style.
