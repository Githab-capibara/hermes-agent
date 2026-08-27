# NN. title in lowercase sentence case

- **Status:** Draft | Accepted | Deprecated
- **Date:** YYYY-MM-DD
- **Type:** Contract
- **Audience:** middleware authors and gateway operators
- **Source files:** `middleware/<name>/`
- **Related:** [adding a platform](../gateway/02-adding-a-platform.md)

## Overview

What this middleware layer does in the request pipeline.

## Interface

Functions or classes that middleware must implement.

```python
class Middleware:
    async def process(request: Request) -> Response:
        ...
```

| Method | Purpose |
|--------|---------|
| `process()` | main hook |
| `teardown()` | cleanup on gateway shutdown |

## Lifecycle

When middleware is initialized, how it receives events, and when it is torn down.

## Configuration

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| … | … | … | … |
