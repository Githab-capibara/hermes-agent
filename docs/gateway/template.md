# NN. title in lowercase sentence case

- **Status:** Draft | Accepted | Deprecated
- **Date:** YYYY-MM-DD
- **Type:** Reference
- **Audience:** operators and contributors working on platform integrations
- **Source files:** `plugins/platforms/<name>/adapter.py`
- **Related:** [adding a platform](./02-adding-a-platform.md)

## Overview

What this platform adapter does and where it fits in the gateway architecture.

## Configuration

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `PLATFORM_TOKEN` | yes | — | Bot token or API key |

## Lifecycle

How the adapter connects, authenticates, and disconnects. Include any reconnect
logic or backoff strategy.

## Message flow

Inbound → outbound mapping. How raw platform events are translated into Hermes
sessions and tool calls.

## Testing

How to test this adapter locally. Link to any fixture data or mock servers.
