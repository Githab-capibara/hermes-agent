# 01. Live test harness

- **Status:** Accepted
- **Date:** 2026-08-23
- **Deciders:** @nousresearch
- **Related:** scripts/tool_search_livetest.py

## Context

Runs five scenarios against a real model to verify bridge tools work end-to-end. Records transcripts in scripts/out/.

## Decision

Document live test harness usage.

## Consequences
- **Easier:** Reproducible verification
- **Harder:** Maintenance
- **Given up:** 
- **Migration:** Moved from scripts/LIVETEST_README.md

## Running

```bash
cd <repo root>
python3 scripts/tool_search_livetest.py
python3 scripts/analyze_livetest.py
```

Requires OPENROUTER_API_KEY set.

## What it verifies

| Scenario | Tests |
|----------|-------|
| A obvious_single | BM25 retrieval |
| B vague_paraphrased | Paraphrase retrieval |
| C multi_tool_chain | Multi-step chaining |
| D core_plus_deferred | Mixed core and deferred |
| E no_tool_needed | No spurious calls |

## Output structure

scripts/out/
  <scenario>__enabled.json
  <scenario>__disabled.json
  _summary.json

