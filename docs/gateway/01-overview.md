# 01. Gateway overview

- **Status:** Accepted
- **Date:** 2026-08-25
- **Type:** Reference
- **Audience:** Gateway developers and operators
- **Source files:** `gateway/run.py` (`GatewayRunner`), `gateway/config.py`, `gateway/platforms/`, `gateway/relay/`, `gateway/session.py`
- **Related:** [Session Lifecycle](../architecture/01-session-lifecycle.md), [Profile Routing](../architecture/02-profile-routing.md), [Relay Connector Contract](../api/01-relay-connector-contract.md), [Adding a platform](02-adding-a-platform.md)

## What the gateway is

`hermes gateway` runs Hermes as a long-lived daemon that connects messaging
platforms to the agent core. One process hosts every enabled platform adapter,
routes inbound messages into sessions, runs agent turns, and delivers replies
back to the originating chat.

## Main components

| Component | Where | Role |
|---|---|---|
| `GatewayRunner` | `gateway/run.py` | Event loop owner. Wires adapters, sessions, agent cache, expiry watcher, restart recovery, message queuing, drain control. |
| Platform adapters | `gateway/platforms/` | Per-platform normalization. `base.py` defines `BasePlatformAdapter`; built-ins include Telegram, Discord, Slack, Signal, WhatsApp Cloud, webhook, api_server, BlueBubbles, WeCom/Weixin, Yuanbao; community platforms ship as plugins under `plugins/platforms/`. |
| Relay adapter | `gateway/relay/` | Dials **out** to an external connector over WebSocket instead of hosting platform sockets itself. See the [Relay Connector Contract](../api/01-relay-connector-contract.md). |
| Session store | `gateway/session.py` | `sessions.json` mapping plus SQLite-backed transcripts. Expiry policies, resume flags, per-user isolation. Detailed in [Session Lifecycle](../architecture/01-session-lifecycle.md). |
| Agent cache | `run.py` + `agent_cache_pressure.py` | LRU cache of warm `AIAgent` instances keyed by session key, with idle-TTL and RSS-pressure eviction. |
| Config | `gateway/config.py` | Platform credentials, reset policies, routing tables, behavior knobs (`require_mention`, home channels, allow-lists). |

## Message path (inbound → reply)

1. Adapter receives a platform event and builds a normalized `MessageEvent`
   with a `SessionSource` (platform, chat ids, thread id, author).
2. `build_session_key()` maps the source to a conversation lane; profile
   routing may retarget the profile before the session is resolved.
3. `get_or_create_session()` resolves the session (honoring suspension,
   resume-pending, and reset policy) and returns or warms the cached agent.
4. The agent turn runs; streaming output goes back through the adapter
   (draft edit / chunked send per platform capability).
5. Delivery helpers handle typing indicators, reactions, media, threads, and
   prompts; failures are retried or degraded per platform.

## Operational surfaces

- Supervision: works under systemd/launchd/s6, containers, tmux, or plain
  foreground. A `.clean_shutdown` marker distinguishes clean restarts from
  crashes ([restart recovery](../architecture/01-session-lifecycle.md#7-restart-recovery-flow)).
- Health export: OTLP metrics/traces/logs — see [Monitoring](../observability/01-monitoring.md).
- Multi-profile deployments: one gateway process per profile, kanban dispatcher
  ownership rules in [Multi-gateway deployment](../kanban/01-multi-gateway.md).

## Adding a platform

New adapters implement the `BasePlatformAdapter` seam set. The step-by-step
guide lives in [Adding a platform](02-adding-a-platform.md).
