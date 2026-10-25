# LibValue AI local prototype

Run `python3 server.py` from this directory, then open http://localhost:4173.

Dependency-free browser application using native JavaScript modules, CSS, SVG charts and browser localStorage. No npm install or external service required. Optional web fonts gracefully fall back to system fonts.

## Demonstration
1. Open Research Methods Archive from the dashboard. Inspect usage, assessment and the earlier cancellation deadline.
2. Open its renewal case. Save a proposed action and rationale, submit for review, then request approval. Switch the top-right demo role to Approver and approve. Export the report using browser Print / Save as PDF.
3. Open Research intelligence and inspect a low-confidence or outside-coverage reference. Confirm or reject with a rationale. Metrics recalculate.
4. Open Usage analytics, download the sample CSV and import it. Repeat the import to verify duplicate detection.
5. Run review checks twice to inspect idempotent alerts. The first simulated email fails and can be retried.
6. View Post-subscription for coverage-verified engagement and interpretation caveats.

## Capability status
Implemented locally: persistent resource CRUD, filters, CSV import with column mapping and validation, deterministic score breakdowns, qualitative edits, renewal workflow and role checks, evidence snapshots, reference review, aggregate engagement, generated template narratives and edits, CSV/JSON exports, print reports, audit history, demo clock and reset.

Simulated: institutional publication retrieval, AI summaries, email delivery, identity/roles, synthetic full-year usage including future months.

Planned: React/TypeScript migration, IndexedDB/server persistence, XLSX/SUSHI ingestion, genuine provider integrations, configurable versioned scoring settings, arbitrary post-subscription windows, package-level relational coverage editor, production authentication and jobs. Coverage table rows are illustrative fixtures. Synthetic references are fixture identifiers and never fetched externally.

Scores use available-weight renormalisation and are withheld below 70% coverage. Quantitative weights: 25/20/15/20/10/10. Qualitative: 20/20/20/15/10/10/5. Combined: 65/35. These rules are demonstration assumptions, not validated library standards.
