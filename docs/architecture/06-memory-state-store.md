# 07. Memory and state store

- **Status:** Accepted
- **Date:** 2026-08-25
- **Type:** Reference
- **Audience:** Contributors working on persistence, search, or portability
- **Source files:** `hermes_state.py` (`SessionDB`), `hermes_state_schema.py`, `hermes_state_search.py`, `hermes_state_portability.py`, `hermes_state_common.py`
- **Related:** [Session Lifecycle](01-session-lifecycle.md), [Micro-compaction](04-micro-compaction.md), [MCP integration](../integration/02-mcp-integration.md)

## Layout

All durable conversation state lives in one SQLite database accessed through
`SessionDB` (`hermes_state.py`, ~13k lines). The class composes four mixins,
one per module:

| Mixin | Module | Responsibility |
|---|---|---|
| `SessionSchemaMixin` | `hermes_state_schema.py` | Table definitions, migrations, row shapes for sessions/messages |
| `SessionSearchMixin` | `hermes_state_search.py` | Full-text session search (FTS5) with LLM summarization of hits — the cross-session recall feature |
| `SessionPortabilityMixin` | `hermes_state_portability.py` | Export/import of session history between homes/profiles |
| (shared helpers) | `hermes_state_common.py` | Paths, atomic writes, common utilities |

## What is stored where

- **SQLite** is the canonical store: message transcripts, session rows with
  end reasons, token/cost accounting, and the FTS index.
- **`sessions.json`** persists only the `session_key → session_id` mapping and
  live entry metadata (flags, timestamps). It is rebuilt from/alongside the
  DB; if SQLite is unavailable the store degrades to JSONL transcripts.
- **Memory-side files** (`MEMORY.md`, `USER.md`, profile `SOUL.md`) are
  agent-curated knowledge, read at prompt-build time rather than queried.

## Invariants the code relies on

- **Append-only flush + soft archive.** Normal writes append; compaction paths
  use `archive_and_compact` to atomically soft-archive replaced rows and insert
  the compacted set, so a resume never loads both the summary *and* the text it
  replaced ([Micro-compaction](04-micro-compaction.md)).
- **End reasons are semantic.** Session rows carry end reasons
  (`session_reset`, `compression`, `agent_close`, …); expiry promotion only
  overwrites recoverable accidental ends, never explicit boundaries.
- **WAL support is probed.** Environments without WAL support raise
  `WalUnsupportedError` and fall back cleanly.
- **Bounded reads.** Resume/export operations guard against oversized payloads
  (`SessionResumeTooLargeError`, `SessionExportTooLargeError`) instead of
  loading unbounded history into memory.

## Who consumes it

- Gateway session store (transcript load/rewrite/rewind) — see
  [Session Lifecycle §3](01-session-lifecycle.md#3-sessionstore--storage-and-operations).
- `/usage`, `/insights`, and cost accounting read per-session token rolls.
- `hermes mcp serve` exposes conversation reads over MCP from this store.
- FTS5 powers cross-session "search my past conversations" in chat.
