# 01. Operations overview

- **Status:** Accepted
- **Date:** 2026-08-25
- **Type:** Reference
- **Audience:** Operators running Hermes on servers/containers
- **Related:** [Monitoring](../observability/01-monitoring.md), [Multi-gateway deployment](../kanban/01-multi-gateway.md), [Session restart recovery](../architecture/01-session-lifecycle.md), [SOUL persona](02-agent-persona-prompt.md), [Network egress isolation](../security/01-network-egress-isolation.md)

## Run modes

| Mode | Command | Use case |
|---|---|---|
| Interactive CLI/TUI | `hermes` | Local use; full terminal UI. |
| Gateway daemon | `hermes gateway start` | Messaging platforms; unattended operation. |
| Containers | `Dockerfile`, `docker-compose.yml` (+ `.windows.yml`) | Serverless-ish hosting, isolation, egress control. |
| Managed/serverless | Daytona / Modal / Vercel Sandbox terminal backends | Hibernates when idle, wakes on demand. |

## Supervision & lifecycle

The gateway runs identically under systemd, launchd, s6, containers, tmux, or
plain foreground. Shutdown writes a `.clean_shutdown` marker; startup without
it triggers crash recovery (`suspend_recently_active`, stuck-loop escalation).
Details: [restart recovery flow](../architecture/01-session-lifecycle.md#7-restart-recovery-flow).

Updates via `hermes update`; interrupted updates that damage TLS state have a
known RCA and guard: [SSL CA bundle corruption](../security/02-rca-ssl-cacert.md).

## Health & telemetry

Enable OTLP export of content-free gauges/lifecycle events:

```yaml
monitoring:
  gateway_health_export:
    enabled: true
```

Verify anytime with `hermes monitoring status`. Full signal table and DataDog
recipe: [Monitoring](../observability/01-monitoring.md).

## Multi-profile operations

Run one gateway per profile (default/writer/admin/coder/researcher); exactly
one owns the kanban dispatcher. Routing inbound communities to per-profile
state: [Profile routing](../architecture/02-profile-routing.md).
Deployment rules: [Multi-gateway deployment](../kanban/01-multi-gateway.md).

## Security posture

- Container network segmentation against prompt-injection exfiltration:
  [Network egress isolation](../security/01-network-egress-isolation.md).
- Exec approvals and DM pairing are gateway-side; trust model:
  [Security policy](../governance/03-security-policy.md).

## Persona

Base persona text and override precedence:
[SOUL.md — agent persona prompt](02-agent-persona-prompt.md).
