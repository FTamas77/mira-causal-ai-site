# mira Causal AI — public website

Live: https://ftamas77.github.io/mira-causal-ai-site/

The website introduces mira through its research questions and applications, not one algorithm, software component or interface.

## Visitor journey

1. **Understand why:** research into causal relationships and effects.
2. **Explore what if:** interventions, counterfactual questions and an interactive, assumption-based simulation.
3. **Make decisions:** compare modeled outcomes against objectives and constraints.
4. **Inspect evidence:** a separate blind synthetic benchmark and three peer-reviewed Q1 research papers.
5. **Connect:** GitHub issues at https://github.com/FTamas77/mira-causal-ai-site/issues/new.

## Pages

- `index.html` — focused capabilities, what-if scenario preview, usage example, benchmark summary and research.
- `demo.html` — synthetic industrial cooling research example and interactive scenario simulator.
- `what-if.js` — small, dependency-free local simulator. It evaluates the explicit hypothetical example equations in the browser. It does **not** connect to the live mira backend.
- `images/cooling-*.svg` — visual illustrations derived from actual reported example results, not original screenshots.
- `benchmark.html` and `benchmark-v2/` — independent 900-row synthetic test with original data, code, prompts and evidence; the score is not a general performance claim.
- `support.html` — optional shortcut to public GitHub issues.
- `privacy.html` and `terms.html` — research-stage notices.

The supplied what-if model computes:
- `energy = 85 + 0.75 × production_load_pct + 0.45 × coolant_flow_lpm`
- `temperature = 68 + 0.15 × (production_load_pct − 65) + 0.22 × (ambient_temp_C − 24) − 0.20 × (coolant_flow_lpm − 50)`
- A candidate is feasible when the modeled temperature is at most 72°C. Among the three reference flows 35/50/65 L/min, the lowest modeled energy feasible candidate is selected.

The coefficients are hypothetical assumptions provided separately from the observational dataset. This browser simulation is illustrative, not automatic SCM fitting, formal individual counterfactual estimation or an industrial operating recommendation.

## Editorial principles

Lead with useful questions, real demonstrations and results. Keep the public copy short, avoid algorithm branding, avoid unnecessary profile links and sponsor disclaimers, and use direct GitHub issue links instead of publishing email addresses. The original research materials and three DOI references remain available. No analytics or trackers are installed.

Updated 20 November 2026.
