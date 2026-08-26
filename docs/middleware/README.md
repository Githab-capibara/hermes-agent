# Hermes Middleware

Middleware is the behavior-changing companion to observer hooks: plugins may
rewrite requests before execution or wrap the execution callback itself.

## Files

| File | Purpose |
|------|---------|
| [01-overview.md](01-overview.md) | Middleware contract — kinds, execution order, examples, safety notes |

## Summary

Four registration kinds cover the LLM and tool paths:

- `llm_request` / `tool_request` — replace effective kwargs/args **before**
  hooks, guardrails, and approvals run.
- `llm_execution` / `tool_execution` — wrap or replace the actual provider/tool
  call via a `next_call(...)` chain.

Chains run in registration order and are fail-open. Full contract, payload
shapes, worked examples, and safety rules:
→ [Middleware contract](01-overview.md).

## Related

→ [Observer hooks (read-only telemetry)](../observability/README.md)
→ [Plugins overview](../plugins/01-overview.md)
