# Design Proposals

This directory contains design proposals for dashboard-native features
and UX improvements. Each document describes a problem, proposes a solution,
and captures the named contracts (tokens, primitives, variants) that
other developers depend on.

## Conventions

- H1 headings are sentence case, starting with the doc number: `# 01. title`.
- Files are numbered sequentially within the directory.
- When a design changes a primitive or token, the change must be reflected
  in this doc **in the same commit** — a stale name is a bug.
- Use [`template.md`](template.md) when writing a new proposal.

## Files

| File | Purpose |
|------|---------|
| [01-profile-builder.md](01-profile-builder.md) | Dashboard-native profile creation |
| [02-desktop-design-system.md](02-desktop-design-system.md) | Desktop app visual and interaction contracts |

## Related

→ [Architecture](../architecture/)
→ [Governance](../governance/)
