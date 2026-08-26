# 06. Cron scheduler

- **Status:** Accepted
- **Date:** 2026-08-25
- **Type:** Reference
- **Audience:** Contributors working on scheduling; operators debugging jobs
- **Source files:** `cron/scheduler.py`, `cron/jobs.py`, `cron/scheduler_provider.py`, `cron/blueprint_catalog.py`, `cron/suggestions.py`, `cron/monitor.py`
- **Related:** [Chronos managed-cron contract](../api/02-chronos-managed-cron-contract.md), [Operations overview](../operations/01-overview.md), [Adding a platform §8](../gateway/02-adding-a-platform.md)

## What it does

The cron system runs scheduled tasks on cron expressions, intervals, or
one-shot times. Jobs execute in **isolated sessions** (no prior context), can
be created by the user in natural language or by the agent itself
(self-scheduled reminders/follow-ups via the `cronjob` tool), and deliver
their results to any connected messaging platform.

## Trigger model

The scheduler is split into a **job store** and a pluggable **trigger
provider**:

- `CronScheduler` ABC (`cron/scheduler_provider.py`) — the "Axis-B trigger
  provider" that decides *when* due jobs fire. Minimal required surface:
  `name` + `start`; Phase-4 hooks (`on_jobs_changed` / `fire_due` /
  `reconcile`) are non-abstract so older providers keep satisfying the ABC.
- `InProcessCronScheduler` — default provider; the gateway daemon ticks it
  every 60 seconds. A file lock prevents duplicate execution if multiple
  processes overlap.
- **Chronos** (`cron.provider: "chronos"`) — hosted scale-to-zero provider
  that arms external one-shots instead of ticking. Wire behavior is specified
  in the [Chronos managed-cron contract](../api/02-chronos-managed-cron-contract.md);
  bundled implementation lives under `plugins/cron_providers/`.

## Job store

`cron/jobs.py` persists desired state (`jobs.json` under the Hermes home) and
exposes the CRUD surface used by tools and CLI: `create_job`, `get_job`,
`list_jobs`, `update_job`, `pause_job`, `resume_job`, `remove_job`. Recurring
jobs advance `next_run_at` under a store lock as part of fire claiming, so
retries never double-run.

Supporting modules:

| Module | Role |
|---|---|
| `blueprint_catalog.py` | Parameterized automation blueprints (`AutomationBlueprint`, slot filling) |
| `suggestions.py` / `suggestion_catalog.py` | Proactive schedule suggestions surfaced to the agent |
| `monitor.py` | Job-health monitoring outcomes |
| `lifecycle_guard.py` | Blocks scheduling actions that would fight gateway lifecycle transitions |

## Platform delivery

Delivery targets resolve through `platform_map` in `_deliver_result()`;
built-in platforms are prewired and plugin platforms register via
`cron_deliver_env_var` (+ optional `standalone_sender_fn` for out-of-process
delivery) — see [Adding a platform](../gateway/02-adding-a-platform.md).

Cron execution lifecycle is exported content-free over OTLP when monitoring
is enabled — see [Monitoring](../observability/01-monitoring.md).
