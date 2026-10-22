# Kelly Wagering

Mathematical foundations, information-theoretic methods, optimization algorithms, and research papers on Kelly wagering, risk, and structured betting markets.

Manuscript author: **Christopher D. Long**.

## Questions raised in the literature

[Whitrow, *Algorithms for Optimal Allocation of Bets on Many Simultaneous Events* (2007), p. 622](https://doi.org/10.1111/j.1467-9876.2007.00594.x) observed that optimal simultaneous bets appear nearly proportional to isolated Kelly stakes and proposed proving this phenomenon.

- **Whitrow's near-proportionality observation** — [Optimal Parlay Wagering and Whitrow Asymptotics](output/pdf/2603.26620-parlays-whitrow.pdf). For independent events with small edges and fixed active support, simultaneous singles-only stakes agree with isolated stakes through second order, with a cubic, event-specific shrinkage. This provides an **asymptotic explanation**.

## Current papers

Each entry links a compiled PDF, its **unaltered arXiv v1 LaTeX source**, and the externally published preprint. Source directories contain SOURCE.md with the original archive checksum.

- **Single-Event Multinomial Full Kelly via Implicit State Positions** — [PDF](output/pdf/2603.13581-implicit-cash.pdf) · [LaTeX](papers/2603.13581-implicit-cash/arxiv-v1/single_event_multinomial_kelly.tex) · [arXiv:2603.13581](https://arxiv.org/abs/2603.13581) · *arXiv v1, original snapshot*
- **Utility-Invariant Support Selection and Eventwise Decoupling for Simultaneous Independent Multi-Outcome Bets** — [PDF](output/pdf/2603.24064-utility-invariant-support.pdf) · [LaTeX](papers/2603.24064-utility-invariant-support/arxiv-v1/utility_invariant_support_decoupling_revised.tex) · [arXiv:2603.24064](https://arxiv.org/abs/2603.24064) · *arXiv v1, original snapshot*
- **Optimal Parlay Wagering and Whitrow Asymptotics** — [PDF](output/pdf/2603.26620-parlays-whitrow.pdf) · [LaTeX](papers/2603.26620-parlays-whitrow/arxiv-v1/optimal_parlay_whitrow_revised.tex) · [arXiv:2603.26620](https://arxiv.org/abs/2603.26620) · *arXiv v1, original snapshot*
- **Risk-Constrained Kelly for Mutually Exclusive Outcomes** — [PDF](output/pdf/2604.11577-risk-constrained.pdf) · [LaTeX](papers/2604.11577-risk-constrained/arxiv-v1/risk_constrained_kelly_prearxiv_final_v2.tex) · [arXiv:2604.11577](https://arxiv.org/abs/2604.11577) · *arXiv v1, original snapshot*
- **Exact Finite-Horizon Quantile Kelly for Repeated Multi-Outcome Events** — [PDF](output/pdf/2604.17577-quantile-kelly.pdf) · [LaTeX](papers/2604.17577-quantile-kelly/arxiv-v1/finite_horizon_quantile_kelly_arxiv_proofread_v4.tex) · [arXiv:2604.17577](https://arxiv.org/abs/2604.17577) · *arXiv v1, original snapshot*

## Paper summaries

### Single-Event Multinomial Full Kelly via Implicit State Positions

[PDF](output/pdf/2603.13581-implicit-cash.pdf) · [LaTeX](papers/2603.13581-implicit-cash/arxiv-v1/single_event_multinomial_kelly.tex) · [arXiv](https://arxiv.org/abs/2603.13581)

For a single event with mutually exclusive outcomes, probabilities $p_i$, and state prices $q_i$, the cash fraction $c$ is a baseline claim on every state. On a positive-cash optimum, a bet is funded only if the probability-to-price ratio exceeds that cash floor; the explicit stake and terminal wealth are

$$
x_i^*=(p_i-c^*q_i)_+,\qquad W_i^*=\max(c^*,p_i/q_i).
$$

The argument leads directly to a sorted likelihood-ratio support algorithm and a compact state-price derivation of the optimal portfolio. The **optimal-stake formula is classical**; the contribution is the implicit-position interpretation and streamlined proof. The later linear-time selection and capped-shadow refinements are recorded separately, not silently inserted into this original submission.

**Status:** arXiv v1 source preserved, compiled PDF available.

### Utility-Invariant Support Selection and Eventwise Decoupling

[PDF](output/pdf/2603.24064-utility-invariant-support.pdf) · [LaTeX](papers/2603.24064-utility-invariant-support/arxiv-v1/utility_invariant_support_decoupling_revised.tex) · [arXiv](https://arxiv.org/abs/2603.24064)

For several independent, finite-outcome events with simultaneous singles-only wagers, this paper isolates the funded-outcome question from the remaining nonlinear allocation problem. Summing active first-order conditions and comparing them with cash stationarity yields a continuation-factor identity that reduces active-support selection to separate single-event likelihood-ratio tests.

Under the specified positive-cash and strictly increasing, strictly concave utility hypotheses, the active support in each event is the same as in that event's isolated optimizer: **support selection is utility-invariant and eventwise**, even though the optimal stake sizes remain coupled. The paper explains the relation to earlier single-event utility-invariance results and does not claim that arbitrary correlated or zero-cash markets decouple.

**Status:** arXiv v1 source preserved, compiled PDF available.

### Optimal Parlay Wagering and Whitrow Asymptotics

[PDF](output/pdf/2603.26620-parlays-whitrow.pdf) · [LaTeX](papers/2603.26620-parlays-whitrow/arxiv-v1/optimal_parlay_whitrow_revised.tex) · [arXiv](https://arxiv.org/abs/2603.26620)

When all singles, doubles, and higher parlays are available at multiplicative prices for independent events, the complete optimal portfolio is the **outer product of the isolated eventwise Kelly strategies**. Consequently, optimal terminal wealth factorizes and a parlay is funded exactly when each of its constituent legs is funded. This gives a short implicit-cash proof of an equivalence previously established by Grant, Johnstone, and Kwon.

Forbidding parlays restricts wealth to an additive profile. On a fixed active support and for small edges $\varepsilon$, a perturbative analysis shows that the simultaneous singles-only optimizer and isolated eventwise optimizer agree through second order, with an event-dependent cubic shrinkage and an $O(\varepsilon^4)$ growth-value penalty compared with the complete parlay menu. It gives a precise asymptotic explanation of the empirical phenomenon posed by Whitrow, with **no universal exact proportionality claim**.

**Status:** arXiv v1 source preserved, compiled PDF available.

### Risk-Constrained Kelly for Mutually Exclusive Outcomes

[PDF](output/pdf/2604.11577-risk-constrained.pdf) · [LaTeX](papers/2604.11577-risk-constrained/arxiv-v1/risk_constrained_kelly_prearxiv_final_v2.tex) · [arXiv](https://arxiv.org/abs/2604.11577)

In a single finite-outcome market, this paper optimizes CRRA utility subject to a drawdown-surrogate restriction on terminal wealth:

$$
\sum_i p_i W_i^{-\lambda}\le 1,\qquad \lambda>0.
$$

Under strict overround and the stated unique likelihood-ratio prefix assumption, imposing this restriction changes the funded wealth amounts but **does not change the active set** relative to the unconstrained solution. For logarithmic utility, the optimizer is obtained through a one-dimensional outer calibration and separate monotone scalar inner solves, with existence and uniqueness proved in the paper.

The exact prefix theorem is not asserted unchanged in fair or subfair markets, where full-support behavior can occur. This distinction is important when transferring support statements to other market models.

**Status:** arXiv v1 source preserved, compiled PDF available.

### Exact Finite-Horizon Quantile Kelly for Repeated Multi-Outcome Events

[PDF](output/pdf/2604.17577-quantile-kelly.pdf) · [LaTeX](papers/2604.17577-quantile-kelly/arxiv-v1/finite_horizon_quantile_kelly_arxiv_proofread_v4.tex) · [arXiv](https://arxiv.org/abs/2604.17577)

For a fixed multi-outcome event repeated independently over a finite horizon, terminal wealth is a monomial in the one-period Arrow–Debreu wealth coordinates, indexed by the multinomial count vector. Its upper quantile is **piecewise monomial on the wealth simplex**, and on each positive-interior count-arrangement chamber, maximizing that quantile is equivalent to solving a Kelly problem for a count-based shadow law.

The manuscript extends the chamber description to faces of the closed simplex, gives a weak exact recursive boundary algorithm, and proves first-order convergence of the optimal scaled log-quantile and its maximizing wealth profiles to ordinary Kelly. Binary and ternary examples illustrate the decomposition. Stronger boundary pruning, finer finite-horizon corrections, and general simultaneous-wager analogues remain open.

**Status:** arXiv v1 source preserved, compiled PDF available.

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

**GitHub Markdown mathematics:** use `$...$` inline and isolated `$$` display blocks separated from prose by blank lines. Never place `=` alone on a line inside an equation: GitHub may parse it as Markdown syntax rather than mathematics. Keep it on the same line as an operand. Avoid custom macros, `\operatorname`, `\,`, `\!`, and brace escapes. The [validator](scripts/validate.py) checks these conventions.

[Paper catalog](papers.json) · [Research status](docs/RESEARCH_STATUS.md) · [PDF builds](output/pdf/) · [LaTeX sources](papers/)
