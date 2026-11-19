# mira Causal AI — research website

The public, static research information site for **mira Causal AI**, a research initiative featuring scientific and engineering work by **Dr. Tamas Fekete**.

Published at: https://ftamas77.github.io/mira-causal-ai-site/

## Pages

- `index.html` — research overview, architecture, capabilities and researcher profile.
- `demo.html` — self-contained synthetic logistics demonstration; does not expose private chats or backend credentials.
- `benchmark.html` — blind causal-discovery benchmark on 900 synthetic observations: 15 TP, 3 FP, 0 FN (precision 83.3%, recall 100%, F1 90.9%) in one reported execution.
- `benchmark-v2/` — the exact benchmark CSV, both original prompts, a reproducible Python generator, evidence JSON and scientific methodology.
- `support.html` — research contact and public issue tracker.
- `privacy.html` — research-stage privacy notice.
- `terms.html` — experimental research-use notice.
- `style.css` and `benchmark.css` — responsive visual styling.

The site uses no JavaScript, analytics, third-party fonts, or trackers. It does not contain the backend source, private MCP configuration, or endpoint secrets.

## Scientific boundaries

The logistics demonstration is a separate, synthetic research example: four contemporaneous and five lagged reference PCMCI+/ParCorr links from a 1,000-row fixture, and an illustrative explicitly supplied SCM with route results A=78 min, B=72 min. These are not measured real-world operational effects.

The current industrial cooling benchmark was a blind, single-dataset evaluation: the generating graph was not supplied to either chat. The private mira v0.4.0 report returned 18 links, of which 15 matched planted lag-1 links and three were additional links. The ChatGPT-only test performed useful descriptive time-lag correlation analysis but did not execute PCMCI+ in that environment. Neither configuration identified causal intervention effects or an optimal operating point. The structured outputs were transcribed from user-shared ChatGPT session reports, not independently replayed.

## Publication notes

Existing website URLs remain stable for ChatGPT app listing metadata, except that the superseded experimental benchmark page and its source artifacts have been intentionally removed. The site does not represent an incorporated company, institutional endorsement, or an approved ChatGPT app. Privacy and terms remain research-stage notices, to be updated as the service evolves.
