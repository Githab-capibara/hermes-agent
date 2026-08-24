# 09. Docs audit todo

- **Status:** Proposed
- **Date:** 2026-08-24
- **Deciders:** @nousresearch
- **Related:** docs/TODO.md

## Context

Documentation is scattered across the repository and does not fully comply with the required style. Need to centralize, number, and standardize.

## Decision

We will create a checklist and execute steps to centralize docs, remove duplicates, fix numbering, and ensure style compliance.

## Consequences

- **Easier:** Single source of truth in /docs
- **Harder:** Need to move many files
- **Given up:** Legacy scattered docs
- **Migration:** Remove source duplicates after verification

## Alternatives considered

- **Option A:** Leave docs scattered. Rejected because violates single source principle.
- **Option B:** Create new docs from scratch. Rejected because existing docs are good.

## Checklist

- [x] Remove docs/TODO.md unnumbered file
- [x] Remove docs/governance/06-todo.md or rename
- [x] Verify docs/governance/07-pull-request-template.md matches .github/PULL_REQUEST_TEMPLATE.md then delete source
- [x] Verify docs/operations/02-soul.md matches docker/SOUL.md then delete source
- [x] Verify docs/governance/08-contributors.md matches contributors/README.md then delete source
- [x] Move providers/README.md to docs/developer-guide/02-providers-registry.md or merge
- [x] Ensure main README has benchmark donut placeholder and SVG architecture links
- [x] Ensure docs/README.md master index with 4 sections
- [x] Ensure each folder has README.md + template.md
- [x] Ensure all files numbered NN-name.md lowercase
