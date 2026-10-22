# Kelly Wagering

Mathematical foundations, information-theoretic methods, optimization algorithms, and research papers on Kelly wagering, risk, and structured betting markets.

Manuscript author: **Christopher D. Long**.

## Questions answered and principal results

The five arXiv manuscripts settle the following **precise mathematical questions under their stated hypotheses**. This is not a claim that they resolve historically named open conjectures; the original single-event optimal-stake formula and parts of Kelly–entropy duality are classical.

- **Can cash and optimal active support be described directly in state-price coordinates?** — [Implicit State Positions](output/pdf/2603.13581-implicit-cash.pdf). Cash creates a baseline in every state, yielding the optimal-stake formula $x_i=(p_i-cq_i)_+$ and a likelihood-ratio threshold.
- **Is the active support for simultaneous independent events utility-invariant?** — [Utility-Invariant Support](output/pdf/2603.24064-utility-invariant-support.pdf). The funded outcomes are exactly the union of eventwise active sets for the paper's utility and positive-cash hypotheses.
- **How does adding parlays change optimal Kelly wagering?** — [Parlays and Whitrow Asymptotics](output/pdf/2603.26620-parlays-whitrow.pdf). The complete multiplicatively priced parlay optimizer factorizes; in a low-edge fixed-support regime, the singles-only growth loss is fourth order and the stake corrections are cubic.
- **Does a CRRA risk constraint alter the funded outcomes?** — [Risk-Constrained Kelly](output/pdf/2604.11577-risk-constrained.pdf). Under strict overround and the unique-prefix hypothesis, the drawdown-surrogate constraint changes the wealth profile but not the active set; logarithmic utility admits scalar calibration.
- **Is exact finite-horizon quantile Kelly reducible to ordinary Kelly subproblems?** — [Finite-Horizon Quantile Kelly](output/pdf/2604.17577-quantile-kelly.pdf). Finite count-arrangement chambers yield shadow-Kelly subproblems, an exact but weak boundary recursion, and first-order asymptotic convergence to ordinary Kelly.

Later [research results and open questions](docs/RESEARCH_STATUS.md) include capped-shadow KL geometry, linear-time support selection, laminar universality, independent singles optimization, fixed-dividend place/show/WPS markets, and endogenous parimutuel liquidity. These are **not yet fully imported as new publication-ready manuscripts**. In particular, a complete fast certified general WPS optimizer remains open.

## Current papers

Each entry links a compiled PDF, its **unaltered arXiv v1 LaTeX source**, and the externally published preprint. Source directories contain SOURCE.md with the original archive checksum.

- **Single-Event Multinomial Full Kelly via Implicit State Positions** — [PDF](output/pdf/2603.13581-implicit-cash.pdf) · [LaTeX](papers/2603.13581-implicit-cash/arxiv-v1/single_event_multinomial_kelly.tex) · [arXiv:2603.13581](https://arxiv.org/abs/2603.13581) · *arXiv v1, original snapshot*
- **Utility-Invariant Support Selection and Eventwise Decoupling for Simultaneous Independent Multi-Outcome Bets** — [PDF](output/pdf/2603.24064-utility-invariant-support.pdf) · [LaTeX](papers/2603.24064-utility-invariant-support/arxiv-v1/utility_invariant_support_decoupling_revised.tex) · [arXiv:2603.24064](https://arxiv.org/abs/2603.24064) · *arXiv v1, original snapshot*
- **Optimal Parlay Wagering and Whitrow Asymptotics** — [PDF](output/pdf/2603.26620-parlays-whitrow.pdf) · [LaTeX](papers/2603.26620-parlays-whitrow/arxiv-v1/optimal_parlay_whitrow_revised.tex) · [arXiv:2603.26620](https://arxiv.org/abs/2603.26620) · *arXiv v1, original snapshot*
- **Risk-Constrained Kelly for Mutually Exclusive Outcomes** — [PDF](output/pdf/2604.11577-risk-constrained.pdf) · [LaTeX](papers/2604.11577-risk-constrained/arxiv-v1/risk_constrained_kelly_prearxiv_final_v2.tex) · [arXiv:2604.11577](https://arxiv.org/abs/2604.11577) · *arXiv v1, original snapshot*
- **Exact Finite-Horizon Quantile Kelly for Repeated Multi-Outcome Events** — [PDF](output/pdf/2604.17577-quantile-kelly.pdf) · [LaTeX](papers/2604.17577-quantile-kelly/arxiv-v1/finite_horizon_quantile_kelly_arxiv_proofread_v4.tex) · [arXiv:2604.17577](https://arxiv.org/abs/2604.17577) · *arXiv v1, original snapshot*

## Paper summaries

### Implicit State Positions

A cash fraction $c$ is equivalent, in terminal-wealth terms, to a baseline state stake $cq_i$ on each outcome. Explicit bets only top up favorable states to their probability weights. The paper gives a short proof of a classical result and an intuitive greedy support rule.

### Utility-Invariant Support and Eventwise Decoupling

For finitely many independent multi-outcome events, the correct continuation-factor identity makes it possible to determine funded outcomes eventwise, in advance of optimizing the chosen strictly increasing, strictly concave utility. Its support theorem requires the paper's precise cash and utility assumptions.

### Optimal Parlay Wagering and Whitrow Asymptotics

An eventwise product of isolated optimal wealth profiles solves the full, multiplicatively priced parlay market. The singles-only restriction has small asymptotic cost in the paper's low-edge regime; the cubic stake correction explains Whitrow's near-proportionality observation.

### Risk-Constrained Kelly

Under strict overround, the CRRA optimizer retains the unconstrained active prefix despite a drawdown-surrogate constraint. For logarithmic utility, the constrained problem reduces to a scalar outer calibration and independent one-dimensional inner solves. The fair and subfair regimes require different treatment.

### Exact Finite-Horizon Quantile Kelly

On each positive-interior count-arrangement chamber, a terminal-wealth quantile is monomial and maximization reduces to a Kelly problem for a shadow empirical law. The full closed simplex requires face stratification and a weak exact boundary recursion. Stronger pruning and higher-order asymptotics remain open.

## Publication and provenance

- **arXiv:** All five papers above are publicly available. Imported sources reproduce the **v1 submissions**, not later working revisions.
- **Other services:** Future versions hosted on **hexagonmath.org** or elsewhere will be listed per paper **after their public links and version identifiers are verified**. No hexagonmath.org submission is claimed here.
- **Repository PDFs:** [output/pdf/](output/pdf/) contains compiled PDFs and a [hash/page manifest](output/pdf/manifest.json).
- **Preservation:** Original arXiv source trees are frozen. Later changes belong in separate revised-manuscript directories with their own external version metadata.
- **Research status:** Unpublished theorems, conditional claims, computations, and open problems are distinguished in [RESEARCH_STATUS.md](docs/RESEARCH_STATUS.md); an internal audit is not independent refereeing.

## Build and checks

On Debian/Ubuntu, install latexmk, texlive-latex-extra, texlive-fonts-recommended, texlive-science, lmodern, and poppler-utils.

```sh
make test       # Check catalog, frozen source blobs, links, and README math
make pdf        # Rebuild the five PDFs and write the SHA-256 manifest
make check      # Check the committed PDFs against catalog and manifest
```

The [PDF build workflow](.github/workflows/build-pdfs.yml) compiles the frozen sources and commits PDFs and a manifest. Compilation alone does not verify mathematical correctness.

**GitHub Markdown mathematics:** use `$...$` inline and isolated `$$` display blocks separated from prose by blank lines. Avoid manuscript-defined macros, `\operatorname`, `\,`, `\!`, and escaped braces in README math. The [validator](scripts/validate.py) enforces the conservative MathJax-compatible subset established for our other repositories.

[Paper catalog](papers.json) · [Research status](docs/RESEARCH_STATUS.md) · [PDF builds](output/pdf/) · [LaTeX sources](papers/)
