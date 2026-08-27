# 07. Subagents and delegation

- **Status:** Accepted
- **Date:** 2026-08-25
- **Type:** Reference
- **Audience:** Contributors working on delegation or parallelism
- **Source files:** `tools/delegate_tool.py`, `tools/async_delegation.py`, `tools/subagent_worktree.py`, `tools/delegation_output_schema.py`, `tools/delegation_live_log.py`
- **Related:** [Observability: subagent hooks](../observability/README.md#subagent-lifecycle), [Monitoring: background gauges](../observability/01-monitoring.md)

## Model

The delegate tool spawns child `AIAgent` instances with isolated context:

- A **fresh conversation** — no parent history leaks into the child.
- An **own `task_id`** — separate terminal sessions and file-op caches.
- **Inherited toolsets** minus child-only blocked tools.
- A **focused system prompt** built from the delegated goal + context.

The parent's context sees only the delegation call and the summary result —
never the child's intermediate tool calls or reasoning.

## Modes

| Mode | Behavior |
|---|---|
| Single task | One child runs the goal; parent waits for the summary. |
| Batch (parallel) | Fan-out of N children run concurrently in a worker pool. |
| Orchestrator children | Top-level calls run in the background; orchestrator-pattern children wait for their own workers so they can synthesize results before returning. |
| Background (`run_in_background`) | Detached delegation tracked by the async pool; surfaced via the `background_work` / `background_delegations` gauges ([Monitoring](../observability/01-monitoring.md)). |

## Supporting machinery

- **Output contracts** — `delegation_output_schema.py` validates structured
  child results so parents can rely on shape, not prose parsing.
- **Worktree isolation** — `subagent_worktree.py` gives code-mutating children
  an isolated git worktree on request, avoiding concurrent edits to one tree.
- **Live log** — `delegation_live_log.py` streams child progress for UIs.
- **Pool accounting** — each async dispatch counts as one delegation unit;
  fan-out batches count N units of *work* but one unit of *pool capacity*
  (`delegation.max_concurrent_children`).

## Observability

Observer hooks `subagent_start` / `subagent_stop` link parent and child via
`parent_session_id` / `child_session_id` and `parent_subagent_id` /
`child_subagent_id`; stop payloads carry a metadata-only tool-call history
(raw arguments and contents excluded). See
[Observer hooks → Subagent lifecycle](../observability/README.md#subagent-lifecycle).
