# NN. title in lowercase sentence case

- **Status:** Draft | Accepted | Deprecated
- **Date:** YYYY-MM-DD
- **Type:** Guide
- **Audience:** skill authors and power users
- **Source files:** `skills/<category>/<name>/SKILL.md`
- **Related:** [skills overview](./01-overview.md)

## Overview

What this skill type does and when to use it.

## Structure

A skill is a directory containing:

| File | Purpose |
|------|---------|
| `SKILL.md` | frontmatter + natural-language description |
| `prompt.md` | system prompt injected at use time |
| `tools/` | optional tool implementations |

## Authoring

How to create a new skill. Link to the full authoring guide.

## Testing

```bash
hermes skills test <skill-name>
```

## Publishing

How to share a skill with the community via the skills registry.
