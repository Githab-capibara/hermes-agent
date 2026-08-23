# 01. Scope plugin manager by Hermes home

- **Status:** Accepted
- **Date:** 2026-07-13
- **Deciders:** @nousresearch
- **Related:** plugins.py, hermes_constants.py, gateway/run.py

## Context

Hermes supports multiple profiles via different Hermes home directories.
Homes are switched two ways in a running process: the `HERMES_HOME`
environment variable (single-profile CLI/gateway processes), and the
context-local `set_hermes_home_override()` (`hermes_constants.py`), which
the multiplexed gateway worker (`gateway/run.py`'s `_profile_scope`) and
subagent/embedded callers use to serve several profiles from one
long-lived process. The override is a `ContextVar` and deliberately does
**not** mutate `os.environ`, since that would leak one profile's home
into every other concurrent task in the same process.

The plugin manager was a process-global single-slot singleton
(`_plugin_manager`). User-installed plugins are discovered from
`get_hermes_home() / "plugins"`, and context-engine plugins (e.g.
`hermes-lcm`) capture profile-scoped state — such as the LCM database
path — at registration time. A single-slot cache meant:

1. Switching homes via `set_hermes_home_override()` was invisible to a
   naive "did `HERMES_HOME` change" check, so the singleton silently kept
   serving the first profile's manager to every other profile in the
   process.
2. Even when a fresh `PluginManager` *was* created for a new home, plugin
   modules are imported into `sys.modules` as `hermes_plugins.<slug>` by
   `_load_directory_module`, and only that top-level module was ever
   replaced. A same-slug plugin's *relative* imports
   (`from . import state`) are cached separately under
   `hermes_plugins.<slug>.<submodule>`, and Python's import machinery
   resolves those from `sys.modules` first — so a profile switch could
   silently keep serving a previous profile's already-imported submodule
   code/state instead of re-executing the new profile's plugin.

## Decision

We replace the single-slot singleton with a cache keyed on the resolved Hermes home path and ensure plugin submodules are evicted on reload or home switch.

- Cache plugin managers by resolved Hermes home: `_plugin_managers_by_home: Dict[Path, PluginManager]`.
- Resolve current home via `get_hermes_home()` which consults `get_hermes_home_override()` before `os.environ`.
- Keep `_plugin_manager` as a thin backward-compatibility pointer; monkeypatches are adopted into the keyed cache.
- Evict `sys.modules[module_name]` and all `module_name + "."` entries before re-import to prevent relative-import leaks.
- Provide `_reset_plugin_managers_for_tests()` to clear cache and purge plugin submodules between tests.

## Consequences

- **Easier:** Per-profile LCM instances use their own `{home}/lcm.db` regardless of switch mechanism. Plugin discovery is cached per profile and reused on re-entry. Profile switching no longer leaks context-engine, module, or submodule state.
- **Harder:** Cache invalidation logic is more complex than a single slot.
- **Given up:** Global singleton semantics for plugin manager.
- **Migration:** Tests that monkeypatch `_plugin_manager` continue to work via adoption into cache; no production code changes required.

## Alternatives considered

- **Option A:** Keep single-slot singleton, add `HERMES_HOME` change detection. Rejected because it would not cover the `set_hermes_home_override()` path which deliberately does not mutate `os.environ`.
- **Option B:** Force full plugin reload on every profile switch. Rejected because it would destroy caching benefits for the common case of returning to a previously-seen profile.
