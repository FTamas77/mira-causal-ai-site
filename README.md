# mira Causal AI — research website

The public, static research information site for **mira Causal AI**, a research initiative featuring scientific and engineering work by **Dr. Tamas Fekete**.

Published at: https://ftamas77.github.io/mira-causal-ai-site/

## Pages

- `index.html` — research overview, architecture, capabilities, three Q1 peer-reviewed publications with publisher DOI links, and researcher profile (ORCID, DBLP and university research coverage).
- `demo.html` — data-driven cooling-system example with visual summaries based on a real synthetic mira run.
- `benchmark.html` — blind causal-discovery benchmark on 900 synthetic observations: 15 TP, 3 FP, 0 FN (precision 83.3%, recall 100%, F1 90.9%) in one reported execution.
- `benchmark-v2/` — the exact benchmark CSV, both original prompts, a reproducible Python generator, evidence JSON and scientific methodology.
- `support.html` — research contact and public issue tracker.
- `privacy.html` — research-stage privacy notice.
- `terms.html` — experimental research-use notice.
- `style.css` and `benchmark.css` — responsive visual styling.
- `favicon.svg` — local branded vector icon.

The site uses no JavaScript, analytics, third-party fonts, or trackers. The publications section links to publishers instead of hosting potentially rights-restricted PDFs. It does not contain the backend source, private MCP configuration, or endpoint secrets.

## Positioning and portfolio scope

**mira is a wider causal AI research and engineering initiative, not a specialized causal-analysis method product or a ChatGPT-only company.** The earlier, more extensive private industrial `mira` codebase explores data preparation, multiple causal-discovery approaches, inference, population-level counterfactual workflows, knowledge management and a standalone web interface. The separate, lean private `mira-causal-ai` backend powers this site's current agent-connected research demonstrations. These are distinct codebases; do not imply their capabilities are merged or production-ready.

ChatGPT/MCP is an early demonstration and potential distribution path. A richer scientific backend, dedicated web product, API or other agent interfaces are future options, not promised features. Vertical focus and packaging should follow customer discovery and funded validation. Technical pages may name a specific algorithm to support reproducibility; high-level marketing copy should lead with evidence, methods, domain knowledge and transparent decisions.

## Website research narrative (20 November 2026)

The homepage now leads with the broader industrial research workflow: data preparation, causal discovery, causal inference, population-level counterfactual/scenario exploration, and the reusable causal knowledge loop. Domain expertise, explicit assumptions, verification and transparency cut across those stages. This is not a claim that every stage runs inside the lightweight ChatGPT connector.

The one-run 900-row benchmark remains a **specific causal-discovery experiment**, not evidence for effect estimation, all algorithms, clinical utility or general product superiority. The current ChatGPT app is an early interface option; MIRA's long-term product may instead use richer science services, the separate web interface or other channels depending on future market validation.

## Public ChatGPT conversation policy

An actual ChatGPT + mira conversation could become a compelling case study, but no full private chat is currently authorized for publication. Before publishing, review the exact original conversation, obtain required permissions, redact private messages, third-party data, keys, private endpoints and internal configuration, and identify what was actually executed. Do not present reconstructed or user-transcribed benchmark records as a verbatim conversation. The existing benchmark materials show prompts and reported results, not a complete original conversation transcript.

## Scientific boundaries

The original logistics illustration was a separate, synthetic research example: four contemporaneous and five lagged reference time-series causal-analysis links from a 1,000-row fixture, and an illustrative explicitly supplied SCM with route results A=78 min, B=72 min. These are not measured real-world operational effects.

The 900-row industrial cooling benchmark was a blind, single-dataset evaluation: the generating graph was not supplied to either chat. The private mira v0.4.0 report returned 18 links, of which 15 matched planted lag-1 links and three were additional links. The ChatGPT-only test performed useful descriptive time-lag correlation analysis but did not execute specialized causal-analysis method in that environment. Neither configuration identified causal intervention effects or an optimal operating point. The structured outputs were transcribed from user-shared ChatGPT session reports, not independently replayed.

## Publication notes

Existing website URLs remain stable for ChatGPT app listing metadata, except that the superseded experimental benchmark page and its source artifacts have been intentionally removed. The site does not represent an incorporated company, institutional endorsement, or an approved ChatGPT app. Privacy and terms remain research-stage notices, to be updated as the service evolves.

## Reviewer-oriented website updates (20 November 2026)

The three journal articles are described as Q1 based on the author's confirmation. All papers link to persistent DOI records and present their actual coauthors and bibliographic metadata. A university research news article is linked as independent evidence of the researcher's contribution, not as an endorsement of mira. Benchmark scoring is explicitly presented as author-run evaluation using previously withheld synthetic ground truth, not an external audit. Existing site, demo, benchmark, privacy, terms, and support URLs are unchanged.
