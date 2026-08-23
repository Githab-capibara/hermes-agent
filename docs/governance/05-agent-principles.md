# 05. Agent principles and documentation standards

- **Status:** Accepted
- **Date:** 2026-08-23
- **Deciders:** @Githab-capibara
- **Related:** AGENTS.md

## Context

The project requires consistent contribution behavior and documentation standards across human and AI contributors.

## Decision

We codify agent principles and documentation standards in English, enforced on all contributors.

### Principles
1. Do not be lazy. Always work at maximum.
2. Before acting, always do reconnaissance. First reconnaissance, then action.
3. Made changes? Update documentation!
4. Added a feature? Update documentation!
5. Made changes? Edit existing tests / write new tests!
6. Added a feature? Edit existing tests / write new tests!
7. Did something? Re-check nothing is broken!
8. Working with system? Be maximally careful!
9. Working with GitHub? Use `gh` command, it is already configured!
10. Making a commit? Always set commit author to user: Nick: "Githab-capibara", Email: "rrrarrr37r@gmail.com"
11. Writing documentation? Follow the style below.
12. See documentation written in wrong style? Fix it!

### Documentation style
A. Architecture Decision Records (ADR)
Format Michael Nygard — strict standard:
# 01. Title in present-tense imperative
- **Status:** Proposed | Accepted | Deprecated | Superseded by ADR-NN
- **Date:** YYYY-MM-DD
- **Deciders:** GitHub handles
- **Related:** links
## Context
...
## Decision
...
## Consequences
...
## Alternatives considered
...

B. Design Documents
# 01. Title
- **Status:** Research note
- **Date:** ...
- **Deciders:** ...
- **Researcher:** ...
- **Purpose:** ...
- **Feeds into:** ...

C. README in subfolders
Table format:
| Guide | Purpose |
|-------|---------|
| [Getting Started](03-getting-started.md) | First engagement in ~5 minutes |

D. Main project README
Badges/shields, hero image/video, benchmark donut chart, architectural SVG diagrams, tables with links to docs.

## Consequences
- **Easier:** Consistent documentation, easier onboarding.
- **Harder:** Requires discipline on every change.
- **Given up:** Informal notes.
- **Migration:** AGENTS.md moved from root to docs.
