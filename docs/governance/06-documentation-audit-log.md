# TODO — Documentation audit & fix

## 1. Language & master index
- [x] Remove Russian text from docs/README.md, keep English only
- [x] Fix broken Code of Conduct link in docs/README.md
- [x] Ensure docs/README.md contains 4 sections: Start here, Directory map, Key entry points, Governance

## 2. Centralize documentation
- [x] Identify project docs outside /docs and move them into /docs with proper folder mapping — moved providers/README.md → docs/developer-guide/01-providers-registry.md and contributors/README.md → docs/governance/04-contributor-email-mapping.md
- [ ] Remove moved files from original locations or leave stubs

## 3. Folder READMEs
- [x] docs/governance/README.md — remove references to non-existent files
- [x] docs/developer-guide/README.md — replace placeholder table with real description
- [x] docs/gateway/README.md — replace placeholder
- [x] docs/integration/README.md — replace placeholder
- [x] docs/middleware/README.md — add description / or note empty — already detailed
- [x] docs/operations/README.md — add description / or note empty
- [x] docs/plugins/README.md — add description / or note empty
- [x] docs/skills/README.md — add description / or note empty
- [x] docs/tools/README.md — add description / or note empty
- [x] docs/troubleshooting/README.md — add description / or note empty
- [x] docs/user-guide/README.md — add description / or note empty

## 4. Main project README
- [x] Add benchmark donut chart placeholder
- [x] Add architectural SVG diagrams placeholder
- [ ] Ensure badges/shields, hero image, tables with links to docs present — already present

## 5. Style compliance
- [ ] Verify all docs files English only
- [ ] Verify filenames lowercase, numbered 01-... in each folder
- [ ] Ensure each folder has README.md + template.md
- [ ] ADR format strict Michael Nygard
- [ ] Design document format correct

## 6. Cross-links
- [ ] Ensure cross-references between docs are valid
- [ ] Update ADR index when new ADR added
