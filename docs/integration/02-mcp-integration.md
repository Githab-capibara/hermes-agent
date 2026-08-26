# 02. MCP integration

- **Status:** Accepted
- **Date:** 2026-08-25
- **Type:** Reference
- **Audience:** Integrators connecting Hermes to MCP ecosystems
- **Source files:** `mcp_serve.py`, `cli-config.yaml.example` (`mcp_servers:`), `optional-mcps/`
- **Related:** [Integration overview](01-overview.md)

Hermes participates in the Model Context Protocol on both sides:

## Hermes as an MCP server

```bash
hermes mcp serve          # stdio MCP server
```

`mcp_serve.py` exposes messaging conversations as MCP tools so any MCP client
(Claude Code, Cursor, Codex, Claude Desktop…) can operate the gateway's
connected platforms remotely:

| Tool | Purpose |
|---|---|
| `conversations_list` | List conversations across platforms |
| `conversation_get` | Fetch one conversation |
| `messages_read` | Read message history |
| `attachments_fetch` | Fetch message attachments |
| `events_poll` / `events_wait` | Poll or block for live events |
| `messages_send` | Send a message into any connected chat |
| `permissions_list_open` | List open approval requests |
| `permissions_respond` | Approve/deny a pending request |
| `channels_list` | Hermes-specific extra: channel directory |

Client registration example:

```json
{
  "mcpServers": {
    "hermes": { "command": "hermes", "args": ["mcp", "serve"] }
  }
}
```

Internally an `EventBridge` fans runtime events into the poll/wait queues;
session reads go through the same SQLite session store the CLI uses.

## Hermes as an MCP client

Attach external MCP servers in `config.yaml`:

```yaml
mcp_servers:
  time:
    command: ["uvx", "mcp-server-time"]
  notion:
    url: https://mcp.notion.com/mcp
```

Both stdio (`command` + `args`) and HTTP/SSE (`url`) transports are supported.
Attached tools appear in the agent's tool namespace and can be scoped through
toolsets; when explicit child toolsets are narrowed,
`inherit_mcp_toolsets: true` keeps the parent's MCP toolsets by default.

`optional-mcps/` ships ready-made server definitions (airtable, asana,
atlassian, comfy-cloud, datadog, figma, hugging_face, intercom, linear, n8n, …)
that can be enabled individually.

Full user-facing documentation:
[website/docs/user-guide/features/mcp.md](../../website/docs/user-guide/features/mcp.md).
