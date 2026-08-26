# 01. Plugins overview

- **Status:** Accepted
- **Date:** 2026-08-25
- **Type:** Reference
- **Audience:** Plugin authors and maintainers
- **Source files:** `hermes_cli/plugins.py` (manager, manifests, discovery), `plugins/` (bundled plugins)
- **Related:** [Middleware contract](../middleware/01-overview.md), [Observer hooks](../observability/README.md), [Plugin architecture lessons](../rfcs/01-plugin-architecture-lessons.md), [Plugin manager state scoping ADR](../adr/01-plugin-manager-state-scoping.md)

## What plugins are

Plugins extend Hermes without touching the agent core: they register observer
hooks, middleware, tools, platforms, cron providers, model providers, and
system-prompt sections. The manager discovers them from three sources:

1. **Bundled plugins** — directories under `plugins/` shipped with the repo.
2. **Entry-point manifests** — installed packages exposing a plugin entry point.
3. **Local/user plugins** — plugin dirs inside the Hermes home.

Each plugin declares itself with a manifest (v2 schema parsed in
`hermes_cli/plugins.py`: name, kind, entry module, config schema, permissions)
and is loaded only when explicitly enabled.

## Bundled plugins

| Directory | Purpose |
|---|---|
| `plugins/browser/` | Browser automation tool provider |
| `plugins/context_engine/` | Context assembly extensions |
| `plugins/cron_providers/` | Alternative cron scheduler backends (incl. Chronos) |
| `plugins/dashboard_auth/` | Dashboard authentication |
| `plugins/disk-cleanup/` | Disk cleanup tooling |
| `plugins/google_meet/` | Google Meet integration |
| `plugins/hermes-achievements/` | Gamification |
| `plugins/image_gen/`, `video_gen/` | Media generation tools |
| `plugins/kanban/` | Kanban work queue system |
| `plugins/memory/` | Memory provider integrations |
| `plugins/model-providers/` | Extra inference providers |
| `plugins/observability/nemo_relay/` | NeMo Relay rich observability exporter |
| `plugins/platforms/line/` | LINE messaging platform adapter |
| `plugins/security-guidance/` | Security policy guidance injection |
| `plugins/spotify/`, `teams_pipeline/`, `web/` | Domain integrations |

## Lifecycle and controls

```bash
hermes plugins list                  # discover
hermes plugins enable <name>         # enable (writes HERMES_HOME state)
hermes plugins disable <name>
```

- Enablement is scoped per Hermes home (see
  [ADR-01: plugin manager state scoping](../adr/01-plugin-manager-state-scoping.md)).
- Load order is resolved by dependency-aware ordering
  (`resolve_plugin_load_order`); failures are fail-open where safe.
- Plugin config is validated against the manifest's declared schema
  (`validate_config_schema`).

## Extension contracts

Plugins interact with the runtime through three stable seams:

| Seam | Doc | Behavior |
|---|---|---|
| Observer hooks | [Observability README](../observability/README.md) | Read-only telemetry; fail-open; return values ignored except legacy compat hooks. |
| Middleware | [Middleware overview](../middleware/01-overview.md) | Rewrite requests/args or wrap execution; registration-order chain; fail-open on raise. |
| Tool/platform/cron/provider registration | manifest kinds | Add new capabilities surfaced to the agent or gateway. |

## Design history

Research that shaped this system (streaming hooks, veto semantics, lifecycle,
manifest versioning) is captured in
[RFC-01: plugin architecture lessons](../rfcs/01-plugin-architecture-lessons.md),
and the config/state bridge slice in
[RFC-02](../rfcs/02-plugin-config-state-bridge.md).
