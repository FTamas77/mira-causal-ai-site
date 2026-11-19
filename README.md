# mira Causal AI — research website

The public, static research information site for **mira Causal AI**, a research initiative featuring scientific and engineering work by **Dr. Tamas Fekete**.

Published at: https://ftamas77.github.io/mira-causal-ai-site/

## Pages

- `index.html` — research overview, architecture, capabilities and researcher profile.
- `demo.html` — self-contained synthetic reference demonstration; does not expose private chats or backend credentials.
- `benchmark.html` — one-run, pre-release ChatGPT-only vs private mira comparison with reported backend evidence.
- `benchmark-cooling/mira_synthetic_cooling_600.csv` — the exact original 600-row synthetic dataset, byte-verified with the generator.
- `support.html` — research contact and public issue tracker.
- `privacy.html` — research-stage privacy notice.
- `terms.html` — experimental research-use notice.
- `style.css` — shared, responsive, accessible visual design.

The site uses no JavaScript, analytics, third-party fonts, or trackers. It does not include backend code or the private MCP configuration.

## Scientific boundaries

The time-series demonstration is synthetic; its 4 contemporaneous and 5 lagged links are reference PCMCI+/ParCorr output on a 1,000-row fixture. The route comparison A=78 min, B=72 min is a **separate, explicitly supplied synthetic SCM example**. These examples are not real-world operational validation, causal effect estimation or automatic SCM fitting.

## Publication notes

The homepage no longer depends on public ChatGPT share links. Existing information URLs are preserved for ChatGPT app listing metadata. Privacy and terms remain research-stage notices; legal, hosting and release eligibility must be checked separately before broader public availability. This site does not represent an incorporated company, institutional endorsement, or an approved ChatGPT app.

## Pre-release benchmark (19 November 2026)

- `benchmark.html`: a sourced, one-run comparison of two ChatGPT configurations on a 600-row synthetic cooling dataset.
- `benchmark.css`: page-specific presentation styles (no JavaScript or trackers).
- `benchmark-cooling/generate_dataset.py`: reproduces the original synthetic CSV with Python's standard library and checks its raw-byte SHA-256.
- `benchmark-cooling/prompt_with_mira.txt` and `prompt_chatgpt_only.txt`: experiment prompts.
- `benchmark-cooling/evidence.json`: the manually transcribed structured results from the user-shared conversation reports, including all 11 links, p-values, partial correlations, request hashes and SCM scenarios.
- `benchmark-cooling/README.md`: explicit data-generating process, evaluation protocol, scientific limits and release retest plan.

The benchmark reported 11/11 synthetic ground-truth edge matches on one specific seeded dataset. It compares *tool availability in tested ChatGPT environments*, not general LLM capability, real-world causal identification or a publicly approved ChatGPT app. The reports came from a private-hosted mira v0.4.0 connector. No server, credential, ChatGPT session dump or live endpoint is published.
