# NN. title in lowercase sentence case

- **Status:** Draft | Accepted | Deprecated
- **Date:** YYYY-MM-DD
- **Type:** Guide
- **Audience:** plugin authors
- **Source files:** `plugins/<name>/`
- **Related:** [adding a platform](../gateway/02-adding-a-platform.md)

## Overview

What this plugin does and which Hermes extension point it hooks into.

## Installation

```bash
hermes plugin install <name>
```

## Configuration

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `PLUGIN_TOKEN` | yes | — | … |

## API surface

Functions, tools, or hooks this plugin exposes.

```python
def my_plugin_hook(context: PluginContext) -> Result:
    ...
```

## Testing

How to test the plugin in isolation and against the full gateway.
