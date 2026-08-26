# 01. Troubleshooting overview

- **Status:** Accepted
- **Date:** 2026-08-25
- **Type:** Reference
- **Audience:** Users and operators diagnosing failures
- **Source files:** `hermes doctor` CLI, `$HERMES_HOME/logs/`
- **Related:** [SSL CA bundle RCA](../security/02-rca-ssl-cacert.md), [Termux constraints](../setup/01-constraints-termux.md), [Monitoring](../observability/01-monitoring.md)

## First moves

```bash
hermes doctor        # diagnoses install, deps, providers, platform wiring
hermes monitoring status   # health-export posture (see observability docs)
```

Logs live under `$HERMES_HOME/logs/` (agent log, gateway log). Structured,
content-free OTLP export is documented in
[Monitoring](../observability/01-monitoring.md).

## Known failure classes

| Symptom | Cause | Doc / fix |
|---|---|---|
| Raw `FileNotFoundError` or opaque SSL error on first provider call | Corrupt/missing CA cert bundle after interrupted update or stale env var | [RCA: SSL CA cert corruption](../security/02-rca-ssl-cacert.md) — surface broken bundles before provider calls |
| Android/Termux install fails on voice/matrix extras | Upstream wheels incompatible with Termux; curated extra required | [Termux dependency constraints](../setup/01-constraints-termux.md) |
| Windows Defender flags `uv.exe` as malware | ML-based AV false positive on unsigned Rust binary | Verify via `gh attestation verify`, whitelist the folder (root README §Troubleshooting) |
| Session lost after gateway restart | Crash without `.clean_shutdown` marker triggers resume-pending flow | [Restart recovery](../architecture/01-session-lifecycle.md#7-restart-recovery-flow) |
| Agent loops/stuck across restarts | Stuck-loop escalation suspends the session after 3+ restarts | Same section — user gets a clean slate by design |
| Messages out of order during bursts | Single-slot pending message + FIFO overflow queue semantics | [Message queuing](../architecture/01-session-lifecycle.md#8-message-queuing-flow) |
| Cron job did not fire while hosted agent slept | Managed cron re-arms one-shots; check Chronos contract path | [Chronos managed-cron contract](../api/02-chronos-managed-cron-contract.md) |
| Micro-compaction slower than expected | Compression model latency dominates per-turn passes | [Micro-compaction §Choosing a compression model](../architecture/04-micro-compaction.md#choosing-a-compression-model) |

## Escalation

When filing an issue include: `hermes doctor` output, relevant tail of
`$HERMES_HOME/logs/`, platform (`hermes --version`, OS), and the config keys
involved (redact secrets).
