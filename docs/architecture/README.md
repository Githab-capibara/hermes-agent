# Architecture

This directory documents the core architecture of Hermes Agent — the design decisions that shape how the agent loop, session management, profile routing, and streaming systems work.

## Contents

| Guide | Purpose |
|-------|---------|
| [Session Lifecycle](01-session-lifecycle.md) | Session data model, lifecycle, and recovery |
| [Profile Routing](02-profile-routing.md) | Multi-profile routing for inbound messages |
| [Streaming TTS](03-streaming-tts.md) | Streaming TTS pipeline architecture |
| [Micro Compaction](04-micro-compaction.md) | Micro-compaction for context management |
| [Cron Scheduler](05-cron-scheduler.md) | Scheduled tasks: job store, trigger providers, delivery |
| [Memory and State Store](06-memory-state-store.md) | SQLite SessionDB, FTS5 search, portability |
| [Subagents and Delegation](07-subagent-delegation.md) | Child-agent isolation, parallel fan-out, background work |

The agent persona prompt reference lives in
[operations/02-soul.md](../operations/02-soul.md).

## Related

→ [ADR Index](../adr/README.md)
→ [API Contracts](../api/README.md)
