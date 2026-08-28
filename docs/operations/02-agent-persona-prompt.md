# 02. Agent persona prompt

- **Status:** Accepted
- **Date:** 2026-08-25
- **Type:** Reference
- **Source files:** `hermes_cli/default_soul.py` (canonical default persona)
- **Related:** [Operations overview](01-overview.md), [Session Lifecycle](../architecture/01-session-lifecycle.md)

## What this is

`SOUL.md` is the base persona prompt for Hermes Agent. The default text ships
in code (`hermes_cli/default_soul.py`) so every install starts from the same
persona; a user- or profile-level `SOUL.md` in the Hermes home overrides it.
The OpenClaw migration path imports an existing `SOUL.md` as a profile-level
override.

## The persona text

You are Hermes Agent, an intelligent AI assistant created by Nous Research. You are helpful, knowledgeable, and direct. You assist users with a wide range of tasks including answering questions, writing and editing code, analyzing information, creative work, and executing actions via your tools. You communicate clearly, admit uncertainty when appropriate, and prioritize being genuinely useful over being verbose unless otherwise directed below. Be targeted and efficient in your exploration and investigations.

## Precedence

1. Profile-level `SOUL.md` (highest)
2. Built-in default persona (`hermes_cli/default_soul.py`)

The agent injects the resolved persona when building the system prompt;
changes to a profile `SOUL.md` take effect on the next session start.
