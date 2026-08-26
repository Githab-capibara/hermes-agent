# 02. Terminal backends

- **Status:** Accepted
- **Date:** 2026-08-25
- **Type:** Reference
- **Audience:** Contributors extending execution environments
- **Source files:** `tools/terminal_tool.py`, `tools/env_probe.py`, `agent/backend_identity.py`, `agent/prompt_builder.py`
- **Related:** [Providers registry](01-providers-registry.md), [Operations overview](../operations/01-overview.md)

## The seven backends

The `terminal` tool executes shell commands through pluggable backends:

| Backend | Kind | Notes |
|---|---|---|
| `local` | host | Direct execution on the host; the default. |
| `docker` | container | Isolated container sandbox. |
| `ssh` | remote | Execution on a remote host over SSH. |
| `singularity` | container | HPC-oriented container runtime. |
| `modal` | serverless container | Serverless persistence — environment hibernates when idle, wakes on demand. |
| `daytona` | serverless container | Same hibernate/wake model as Modal. |
| `vercel_sandbox` | serverless container | Vercel-hosted sandbox. |

Container-class backends are declared in
`tools/terminal_tool.py` (`_CONTAINER_BACKENDS = {docker, singularity, modal,
daytona, vercel_sandbox}`); remote sets are mirrored in
`agent/prompt_builder.py` and `tools/env_probe.py` so prompts and environment
probes know when commands run off-host.

## Working-directory rules

A container's cwd must be an absolute path that exists *inside* the sandbox.
`_is_unusable_container_cwd()` detects host/relative paths (`/home/...`,
`C:\...`, `.`, `src/`) before they reach `docker run -w` (which would fail with
exit 125) and rewrites or rejects them.

## Backend identity

`agent/backend_identity.py` provides a `BackendIdentity` value type used to
classify failures and compare environments across backends, so retry logic can
distinguish "same backend, transient error" from "different backend".

## Adding one

1. Extend the backend dispatch in `tools/terminal_tool.py`.
2. Add the backend to `_CONTAINER_BACKENDS` if it is containerized, and to the
   remote sets in `prompt_builder.py` / `env_probe.py` if it is off-host.
3. Cover cwd handling and failure classification in tests.

Serverless backends should follow the Modal/Daytona pattern: cheap while idle,
resumable sessions across invocations.
