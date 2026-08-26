# 01. User guide overview

- **Status:** Accepted
- **Date:** 2026-08-25
- **Type:** Reference
- **Audience:** End users
- **Related:** [Setup guides](../setup/README.md), [Troubleshooting](../troubleshooting/01-overview.md), [Skills](../skills/01-overview.md), [Full docs site](https://hermes-agent.nousresearch.com/docs/)

## Two entry points

| Surface | Start with | Notes |
|---|---|---|
| Terminal | `hermes` | Full TUI: multiline editing, slash-command autocomplete, streaming tool output, session history. |
| Messaging | `hermes gateway setup` → `hermes gateway start` | Talk from Telegram, Discord, Slack, WhatsApp, Signal, Email; same agent core and slash commands. |

## Everyday commands

```bash
hermes              # interactive CLI
hermes model        # pick provider/model
hermes tools        # enable/disable toolsets
hermes config set   # set config values
hermes setup        # full setup wizard
hermes update       # update
hermes doctor       # diagnose problems
```

In-conversation slash commands work on both surfaces: `/new`, `/retry`,
`/undo`, `/compress`, `/usage`, `/insights`, `/model`, `/personality`,
`/skills`, `/<skill-name>`, plus platform-specific `/status`, `/platforms`.

## What you can do from chat

- **Automate on a schedule** — natural-language cron ("every night at 2am,
  back up X"), delivered to any connected platform.
- **Delegate** — spawn isolated subagents for parallel workstreams.
- **Build memory** — agent-curated MEMORY.md / USER.md, session search across
  past conversations.
- **Use skills** — procedural memory invoked as `/<skill>`; Hermes creates and
  improves skills autonomously ([Skills](../skills/01-overview.md)).
- **Approve dangerous commands** — exec approvals with once/session/always
  choices, DM pairing, container isolation.

## Where to go next

- Install & first run → [Setup guides](../setup/README.md)
- Something broken → [Troubleshooting overview](../troubleshooting/01-overview.md)
- Provider/model choices → [Providers registry](../developer-guide/01-providers-registry.md)
- Deep reference per feature (CLI, messaging, security, tools, memory, MCP,
  cron, context files) → the [docs site](https://hermes-agent.nousresearch.com/docs/)
