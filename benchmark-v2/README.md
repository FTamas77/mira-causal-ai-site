# Blind industrial cooling benchmark v2 — 19 November 2026

## Status and evidence standard

Two separate ChatGPT conversations received the same **900-row synthetic time series** and matching core instructions. Only one was allowed to use the connected **private mira Causal AI v0.4.0** scientific backend. The other used built-in Python and already-installed scientific packages; it was explicitly prohibited from installing or improvising PCMCI+. The original seeded generating graph was held out from **both** chats until the user shared their answers. This is a capability-availability experiment in two environments, not a claim that ChatGPT could never run the method with a working Tigramite installation.

The mira operation and parameters are **reported in a user-provided ChatGPT transcript**. The original raw MCP request/response has not been independently re-executed for publication. The baseline report likewise comes from the user. A separate local check verified the original CSV bytes and scored all 18 reported links against the exact planted generating graph.

Files:
- `mira_blind_cooling_v2_900.csv`: the same original CSV uploaded to both conversations, SHA-256 `22eac3fc04f0577df3af126d5537c628018213e1dcfd35cef5f304b2aeb5d13a`.
- `generate_dataset.py`: Python-standard-library generator, verifies the exact CSV checksum. Burn-in: 250; seed: 20261119.
- `prompt_with_mira.txt`, `prompt_chatgpt_only.txt`: exact original prompts from both runs.
- `evidence.json`: every reported backend edge, its test statistics, baseline evidence, and graded metrics.

## Hidden synthetic model (disclosed after the runs)

Independent Gaussian disturbances with SDs shown below. Six variables: ambient A, production load L, coolant flow F, machine temperature M, energy E, vibration V.

```text
A(t) = 20  + 0.62*(A(t-1)-20) + noise, SD 1.25
L(t) = 60  + 0.55*(L(t-1)-60) + noise, SD 1.40
F(t) = 100 + 0.38*(F(t-1)-100) + 1.20*(L(t-1)-60)
           + 0.85*(M(t-1)-55) + noise, SD 1.10
M(t) = 55  + 0.50*(M(t-1)-55) + 0.56*(L(t-1)-60)
           - 0.55*(F(t-1)-100) + 0.26*(A(t-1)-20) + noise, SD 0.85
E(t) = 40  + 0.36*(E(t-1)-40) + 0.38*(L(t-1)-60)
           + 0.25*(F(t-1)-100) + noise, SD 0.90
V(t) = 8   + 0.42*(V(t-1)-8) + 0.44*(M(t-1)-55)
           + 0.22*(L(t-1)-60) + noise, SD 0.75
```

There are **15 direct lag-1 structural edges**: six self-lag edges and nine cross-variable edges. **No direct lag-0 or lag-2 edges were planted**. The key bidirectional feedback is F(t−1)→M(t) (negative) and M(t−1)→F(t) (positive). Discovery alone does not estimate these structural coefficients.

## Grading method and result

Compare every backend-reported source/target/lag triple against the structural parent sets from the generator. Each correctly matched triple is one TP; each unmatched reported triple is one FP; each planted triple absent from the report is one FN.

- Reported PCMCI+ links: 18 total (16 lagged, 2 same-time).
- Ground truth: 15 planted links, all at lag 1.
- **TP=15, FP=3, FN=0**.
- Precision 15/18 = 83.33%; recall 15/15 = 100%; F1 = 30/33 = 90.91%.
- Cross-variable only: 9 TP, 3 FP, 0 FN; precision = 75%; recall = 100%; F1 = 85.71%.
- True autoregressive self-links: 6/6.
- The three unmatched edges are: M(t)→V(t), L(t)→F(t), and V(t−1)→F(t). They are **false positives relative to the known generating graph**, not proof of bugs or fabricated statistics.
- The two same-time edges have p=0.01921 and p=0.04006; the unmatched V→F lag-1 edge has p=0.004863. No multiple-testing correction was used in this test.

The baseline performed ordinary Pearson correlations, including F vs M at lag 0: +0.05625, lag 1: −0.67497, lag 2: −0.78542. The largest-magnitude raw Pearson correlation was lag 2, yet the planted *direct* link was lag 1. This discrepancy illustrates why conditioning and temporal discovery can be important. It does not establish causal effects.

## What this proves and what it does not

**Supported:** In the reported environment, mira executed specialized PCMCI+ / analytic ParCorr and returned a structured graph which recovered all planted links in one synthetic dataset, plus three false positives; the baseline produced useful descriptive evidence but could not import Tigramite. Both correctly declined to fabricate an SCM effect or optimize cooling flow without structural model identification.

**Not supported:** universal superiority over ChatGPT, production performance, identified real-world intervention effects, automatic SCM fitting, or a public ChatGPT app approval. This is one test with no independent replicated trials and no correction for multiple hypothesis testing.

After public release, repeat with the public connector, several hidden independently seeded datasets, different structural regimes, multiple trials, and fully captured raw backend evidence. Report error rates, execution failures, end-to-end time, and scientific interpretability—alongside the benefits of having a stable, reusable tool.
