# Industrial cooling: pre-release ChatGPT + mira benchmark (19 November 2026)

## Evidence status

This is a single-user, single-run comparison with a **private-hosted** mira Causal AI v0.4.0 connector and a separate ChatGPT-only conversation. Exact user-shared response details are transcribed in `evidence.json`. They are a *reported backend execution*, not a raw machine-captured audit log independently reproduced here. ChatGPT-only installation failed due to unavailable network access; this is an environment observation, **not** an assertion that ChatGPT is incapable of causal analysis.

The original 600-row CSV is directly downloadable as [`mira_synthetic_cooling_600.csv`](mira_synthetic_cooling_600.csv) and also reproducible from `generate_dataset.py` (Python standard library, seed 20261119, 200 burn-in records, six CSV columns including timestamp). Raw CSV SHA-256: `f2e58076228e324bae48237bc10cb585a28aa98265d4ab60bc1a57b841ad1cf4`. Run `python generate_dataset.py` in this directory; the script checks the checksum and fails if bytes differ. The original CSV was byte-for-byte checked against Git blob SHA-1 `aa8e2ee9fed366fce21de47d45705f1dc69f5780` and SHA-256 `f2e58076228e324bae48237bc10cb585a28aa98265d4ab60bc1a57b841ad1cf4`. The original prompts are included as downloadable text files, with formatting normalized and the scientific instructions unchanged.

## Ground-truth structural data-generating process

All innovations are **independent Gaussian draws**. Let A=ambient temperature, L=production load, F=coolant flow, M=machine temperature, E=energy. Every right-hand-side parent is at time t−1.

```text
A(t) = 20  + 0.62*(A(t-1)-20) + N(0,1.4)
L(t) = 60  + 0.45*(L(t-1)-60) + N(0,1.3)
F(t) = 100 + 0.42*(F(t-1)-100) + 0.72*(L(t-1)-60) + N(0,1.8)
M(t) = 55  + 0.46*(M(t-1)-55) + 0.32*(L(t-1)-60)
          - 0.38*(F(t-1)-100) + 0.35*(A(t-1)-20) + N(0,1.1)
E(t) = 40  + 0.46*(E(t-1)-40) + 0.28*(L(t-1)-60)
          + 0.22*(F(t-1)-100) + N(0,1.0)
```

**11 planted lag-1 links:** five autoregressive links (A→A, L→L, F→F, M→M, E→E) and six cross-variable links (A→M, L→F, L→M, L→E, F→M, F→E). No lag-0 or lag-2 structural links planted.

The 11 source/target/lag triples reported by mira are exactly those 11 planted links: TP=11, FP=0, FN=0; precision=recall=F1=1.0 **on this one synthetic dataset**. This exact count does not imply generalization or treatment-effect identification. Partial correlations are conditional-independence test statistics, not effect coefficients; the 11 identified arrows have lag-1 temporal direction. No correction for multiple testing in this benchmark.

## Separate explicit-SCM comparison

The treatment test holds other lagged states at their reference means and all innovations at zero. It supplies these two equations directly, rather than learning them from discovery:
```text
M(t) = 55 - 0.38*(F(t-1)-100)
E(t) = 40 + 0.22*(F(t-1)-100)
```
A=100 L/min: 55°C, 40 kWh → fails ≤53°C. B=110 L/min: 51.2°C, 42.2 kWh → passes, only feasible. Both configurations correctly choose B under an objective of minimizing energy subject to the temperature limit. This is one-step conditional scenario evaluation, **not an individualized historical counterfactual**.

## What this case study does and does not establish

- **Demonstrated in the shared reports:** the specialized mira connector returned PCMCI+/ParCorr results in the tested environment, including 11 lagged links, structured statistics and reproducibility hashes; the ChatGPT-only environment could not install Tigramite and transparently reported PCMCI+ not run.
- **Not a differentiator in this test:** both configurations evaluated the supplied SCM and recommended the same feasible scenario. The plugin's benefit here is **specialized execution availability, structured statistical output and computation provenance**, not unique access to basic arithmetic.
- **Not demonstrated:** broad model accuracy, production-scale reliability, real-world causal identification, causal effect estimation, fitting an SCM from observational data, or any difference in language-model reasoning ability.
- The mira backend initially rejected one malformed SCM request; the client corrected the schema and the second request completed. This is included rather than hidden.
- The server was **private_hosted**; successful use here does not establish public ChatGPT app publication or review approval.
- The figures derive from the user-supplied follow-up response, not from a new independent rerun. The public hashes identify reported backend inputs; they do not alone prove that a fresh run would match.
- Re-run with the public app and multiple independently seeded datasets after release. Keep model/settings and data identical between configurations and report variance and failures.
