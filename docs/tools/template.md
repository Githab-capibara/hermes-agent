# NN. title in lowercase sentence case

- **Status:** Draft | Accepted | Deprecated
- **Date:** YYYY-MM-DD
- **Type:** Reference
- **Audience:** contributors adding or extending tools
- **Source files:** `tools/<name>.py`
- **Related:** [toolsets overview](./03-toolsets-distribution.md)

## Overview

What this tool does and which toolset it belongs to.

## Signature

```python
@tool(description="...")
async def tool_name(param: str) -> ToolResult:
    ...
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `param` | string | yes | … |

## Return schema

What `ToolResult` carries back to the agent.

## Permissions

Which toolset(s) expose this tool and whether it requires approval.

## Examples

Sample tool call and response.
