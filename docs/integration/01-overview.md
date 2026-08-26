# 01. Integration overview

- **Status:** Accepted
- **Date:** 2026-08-25
- **Type:** Reference
- **Audience:** Integrators and power users
- **Source files:** `providers/` (registry), `mcp_serve.py`, `gateway/platforms/`, `gateway/relay/`
- **Related:** [Providers registry](../developer-guide/01-providers-registry.md), [Gateway overview](../gateway/01-overview.md), [Relay Connector Contract](../api/01-relay-connector-contract.md), [MCP integration](02-mcp-integration.md)

## Integration surfaces

Hermes integrates outward in four directions. Each has a dedicated contract
document:

| Surface | What it connects | Doc |
|---|---|---|
| Model providers | Any LLM endpoint: Nous Portal, OpenRouter, OpenAI-compatible, Anthropic, Bedrock, Azure, local servers | [Providers registry](../developer-guide/01-providers-registry.md) |
| Messaging platforms | Telegram, Discord, Slack, Signal, WhatsApp, and ~20 more via gateway adapters | [Gateway overview](../gateway/01-overview.md) |
| External connector (relay) | A Node/TypeScript connector fronts shared bots; the gateway dials out over an authenticated WebSocket | [Relay Connector Contract](../api/01-relay-connector-contract.md) |
| MCP (Model Context Protocol) | Hermes as an MCP **server** exposing sessions/events, plus MCP **client** support for attaching external MCP servers | [MCP integration](02-mcp-integration.md) |

## Provider model

Every provider is declared once as a `ProviderProfile` in `providers/`; auth
resolution, transport kwargs, model listing, and routing all read from the
registry instead of per-feature parallel tables. Credentials resolve through a
single chain: config → env/`.env` → credential pool — never bare env reads.

## Platform model

Platform adapters normalize wire events into `MessageEvent` + `SessionSource`.
Native adapters live in `gateway/platforms/`; community platforms (e.g. LINE)
ship as plugins under `plugins/platforms/`. The relay lane replaces direct
sockets with an outbound dial to a connector for hosted/shared-bot setups.

## Tool Gateway (Nous Portal)

With `hermes setup --portal`, one subscription supplies web search, image
generation, TTS, and a cloud browser alongside models. The gateway is
per-tool-backend: bring-your-own keys remain possible per tool.

## Adding integrations

- New platform adapter → [Adding a platform](../gateway/02-adding-a-platform.md)
- New provider → follow the registry pattern in
  [Providers registry](../developer-guide/01-providers-registry.md)
- New MCP server attachment → [MCP integration](02-mcp-integration.md)
