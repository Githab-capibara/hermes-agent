# Documentation Audit TODO

## Phase 1 – Centralize docs
- [x] Move root AGENTS.md to docs/governance with English translation, numbered 05-agent-principles.md
- [x] Remove duplicate constraints-termux.txt from root (already in docs/setup/01-constraints-termux.md)
- [x] Remove docs/TODO.md from root docs or renumber/move to appropriate folder
- [x] Identify and move markdown docs from scripts/, docker/, .github/ into docs/* with proper numbering

## Phase 2 – Style compliance
- [x] Ensure docs/README.md contains 4 sections: Start here, Directory map, Key entry points, Governance with cross-links
- [x] Verify all docs files are English only
- [x] Ensure every documentation file is numbered NN-name.md, lowercase, 2-3 words
- [x] Ensure each folder has README.md + template.md
- [x] ADR format check for docs/adr/*
- [x] Design doc format check for docs/design/*

## Phase 3 – Completeness
- [x] Fill empty folders gateway, integration, middleware, operations, plugins, skills, tools, troubleshooting, user-guide with at least placeholder docs
- [x] Update main project README.md badges/shields, hero, benchmark donut, architecture SVG, docs links

## Phase 4 – Cleanup
- [x] Remove moved source files or leave stubs
- [x] Update git commit author
- [x] Run tests to ensure no breakage
