# 01. Termux/Android dependency constraints

- **Status:** Accepted
- **Date:** 2026-08-25
- **Type:** Reference
- **Source files:** `scripts/install.sh`, `setup-hermes.sh` (consumers), `tests/test_termux_all_extra_compat.py` (regression coverage)
- **Related:** [Troubleshooting overview](../troubleshooting/01-overview.md), [Termux install guide (docs site)](https://hermes-agent.nousresearch.com/docs/getting-started/termux)

## Why these pins exist

Upstream packages move faster than Termux-compatible wheels and sdists. The
pins below keep the tested Android install path stable: they cap or floor
transitive dependencies of the IPython stack that currently have no
Termux-compatible release in newer versions.

## The pins

| Package | Constraint | Reason |
|---|---|---|
| `ipython` | `<10` | Newer majors ship no Termux-compatible wheel/sdist path |
| `jedi` | `>=0.18.1,<0.20` | Known-good completion core on Android |
| `parso` | `>=0.8.4,<0.9` | Pinned with jedi compatibility window |
| `stack-data` | `>=0.6,<0.7` | IPython dependency kept on tested line |
| `pexpect` | `>4.3,<5` | PTY handling behavior relied upon on Termux |
| `matplotlib-inline` | `>=0.1.7,<0.2` | IPython inline plotting pin |
| `asttokens` | `>=2.1,<3` | IPython dependency kept on tested line |

## How they are applied

Installers pass the constraints file to pip via `-c`:

```bash
python -m pip install -e '.[termux]' -c constraints-termux.txt
```

`scripts/install.sh` tries, in order:

1. `.[termux-all]` with constraints (broad profile)
2. `.[termux]` with constraints (baseline curated profile)
3. plain `.` base install as last resort

The machine-readable `constraints-termux.txt` used at install time ships with
the installer layout; this page documents what it contains and why. Regression
coverage lives in `tests/test_termux_all_extra_compat.py`.

## Note on voice extras

The full `.[all]` extra currently pulls Android-incompatible voice
dependencies; on Termux use the curated `.[termux]` / `.[termux-all]`
profiles instead.
