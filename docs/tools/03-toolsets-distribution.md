# 03. Toolsets and distributions

- **Status:** Accepted
- **Date:** 2026-08-25
- **Type:** Reference
- **Audience:** Contributors configuring tool exposure; datagen operators
- **Source files:** `toolsets.py` (`TOOLSETS`), `toolset_distributions.py`, `datagen-config-examples/`
- **Related:** [Adding a platform §7](../gateway/02-adding-a-platform.md), [MCP integration](../integration/02-mcp-integration.md), [Core-toolset A/B harness](02-toolperf-abeval.md)

## Toolsets

`toolsets.py` defines named bundles of tools in the `TOOLSETS` registry. Each
entry has:

```python
"<name>": {
    "description": "...",
    "tools": [...],        # explicit tool names
    "includes": [...],     # other toolsets pulled in wholesale
}
```

Representative sets: `web`, `search`, `x_search`, `vision`, `video`,
`image_gen`, `video_gen`, `bfl`, `computer_use`, `terminal`, plus composite
profiles like `hermes-gateway` that `include` platform-specific sets.
Platform integrations add their own named toolset and register it inside the
gateway composite ([Adding a platform §7](../gateway/02-adding-a-platform.md)).
MCP-attached toolsets follow the same namespace and honor
`inherit_mcp_toolsets` when child toolsets are narrowed.

Selection at runtime happens through `hermes tools` / `/tools` or config;
`validate_toolset()` guards references against unknown names.

## Distributions (data generation)

`toolset_distributions.py` is the batch-runner counterpart: a **distribution**
maps toolset names to selection probabilities for data-generation runs:

```python
DISTRIBUTIONS = {
    "default": {...},       # every toolset available 100%
    "image_gen": {...},     # weighted mix biased to image generation
    ...
}
```

API: `get_distribution(name)` returns one distribution;
`list_distributions()` enumerates them. Probabilities are normalized if they do
not sum exactly to 100. Worked configs live in `datagen-config-examples/`.

Together these two modules drive both what a live agent may call and how
training-data batches sample tool exposure — the same vocabulary in both
places is deliberate.
