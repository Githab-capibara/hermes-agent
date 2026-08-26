# 02. Terminal UI overview

- **Status:** Accepted
- **Date:** 2026-08-25
- **Type:** Reference
- **Audience:** End users of the desktop terminal experience; TUI contributors
- **Source files:** `ui-tui/` (application), `tui_gateway/` (host bridge)
- **Related:** [User guide overview](01-overview.md), [Billing lifecycle](../api/03-billing-lifecycle.md)

## What it is

`hermes` launches the full-screen terminal UI — a TypeScript application under
`ui-tui/` rendered in the terminal. It is the richest local surface onto the
same agent core the gateway uses.

## Features

- Multiline editing with slash-command autocomplete.
- Conversation history browsing; interrupt-and-redirect of running turns.
- Streaming tool output while the agent works.
- Slash-command parity with messaging surfaces (`/model`, `/retry`, `/undo`,
  `/compress`, `/usage`, `/insights`, `/skills`, …).
- Billing and subscription overlays with typed state handling — every NAS
  billing state and refusal code has an explicit render path
  ([Billing lifecycle](../api/03-billing-lifecycle.md)).

## Architecture map

```
ui-tui/
  src/app/            # screens & app shell
  src/components/     # overlays (billing, subscription), widgets
  src/protocol/       # wire protocol types shared with the host
  src/sdk/            # client SDK used by the app
  src/gatewayClient.ts# connection to the local gateway host

tui_gateway/
  host_supervisor.py  # supervises the agent/gateway process behind the TUI
  compute_host.py     # compute-side host services
  event_publisher.py  # streams events to the UI
  entry.py            # entry point wiring
```

The Python side (`tui_gateway/`) owns process supervision and event streaming;
the TypeScript side renders. MCP OAuth session handling for hosted flows lives
in `tui_gateway/mcp_oauth_sessions.py`.

## When to use which surface

| Need | Surface |
|---|---|
| Local interactive work, full keyboard UX | TUI (`hermes`) |
| Talk from phone / unattended automation | Gateway (`hermes gateway start`) |
| Scripted/CI usage | `hermes chat --query '...'` or batch runner |
