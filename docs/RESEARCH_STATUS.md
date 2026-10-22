# Research status and open problems

This is a **research ledger**, not an additional submitted manuscript. Claims developed after the five arXiv submissions have heterogeneous proof and verification status; no unimported manuscript is represented as reviewed, published, or included in this repository.

## Submitted papers

| arXiv | Topic | State |
| --- | --- | --- |
| [2603.13581](https://arxiv.org/abs/2603.13581) | Implicit cash and single-event support | Original v1 imported, PDF built from source |
| [2603.24064](https://arxiv.org/abs/2603.24064) | Simultaneous independent-event utility-invariant support | Original v1 imported, PDF built from source |
| [2603.26620](https://arxiv.org/abs/2603.26620) | Parlays and Whitrow asymptotics | Original v1 imported, PDF built from source |
| [2604.11577](https://arxiv.org/abs/2604.11577) | Risk-constrained CRRA support | Original v1 imported, PDF built from source |
| [2604.17577](https://arxiv.org/abs/2604.17577) | Finite-horizon quantile Kelly | Original v1 imported, PDF built from source |

The listed publication status means a public arXiv preprint, **not** journal acceptance.

## Unpublished results and developing manuscripts

The October 16, 2026 Kelly master research record, version 1.5, is the more comprehensive mathematical and evidence ledger. Its full source has **not** yet been imported here. Items below are a map of that work, not claims of newly reproduced or independently refereed proofs.

### Information geometry of overround Kelly

- Capped-shadow representation with $s_i^*=\min(q_i,p_i/c^*)$, where the normalizer satisfies $ \sum_i\min(q_i,p_i/c^*)=1 $.
- Reverse-KL projection over the price-capped simplex; active/inactive coarsening, exact regret identities, projection inequalities, Pinsker-style estimates, and model-versus-allocation regret.
- Median-based deterministic $O(n)$ arithmetic active-set selection using cumulative active price and inactive probability masses. Distinguish the classical optimizer from the later algorithmic presentation and specialized consequences.
- **Status:** derivations and audit material in the master record; not an added public paper. The classical Kelly–entropy relation and general selection ingredients have antecedents.

### Independent markets and laminar utilities

- Two-event contraction and symmetric M-matrix Jacobian for singles-only independent events; cash-plus-event block updates and transform oracles.
- Laminar capped-shadow recursion, with a meldable-heap arithmetic implementation.
- Level-set replication criteria for utility-independent shadow laws; positive-polar polymatroid and fixed-price effective-rank criteria; all-positive-price indicator universality/laminar classification.
- **Status:** research results with explicit hypotheses, counterexamples, and priority qualifications recorded in the master. The classification theorems merit independent theorem-level and literature review before promotion to final manuscripts.
- **Open:** uniformly fast certified optimization for arbitrary heterogeneous independent singles menus of three or more events; a general near-linear overlapping-menu solver.

### Utility, robustness, and hedging

- CRRA, Rényi, CARA/DARA completion, bid–ask projection, proportional fairness and majorization, robust no-trade thresholds, model uncertainty, and new-claim reservation prices.
- Cash-aware first-order finite-IID quantile asymptotics are developed; the **finite-horizon simultaneous-event chamber extension** is not established.
- An older wealth-profile/hedging research draft covers endowments, convex trading costs, and dynamic rehedging; it has not yet been imported as a ready-to-compile standalone paper.
- **Status:** overlapping result packages with different assumptions; avoid treating them as one universal utility theorem.

### Parimutuel self-impact

- A specified idealized nonlinear single-winner pool admits exact mixture/two-KL identities, convex final-pool coordinates, a two-scalar solve, and exact-rational global gap certificates.
- Large-pool liquidity loss has a chi-square leading term. The unadjusted benchmark has second-order allocation regret; a rank-two correction gives fourth-order regret under strict support separation and other stated hypotheses.
- **Critical boundary:** affine fixed-price shadow normalization and support transfer do **not** hold unchanged for endogenous payouts.
- **Open:** multi-winner pool payout models, impact-corrected place/show/WPS, and a sufficiently general certified end-to-end implementation.

### Fixed-dividend place, show, and WPS

- State-wealth incidence/hypergraph formulation; active-pattern coarsening and sparse inclusion-marginal oracles; structured product-weight and low-rank ordered-finish kernels; small correlated examples.
- Exactly checked counterexamples refute an overgeneralized greedy no-pruning conjecture. Narrower support hypotheses remain to be investigated.
- **Status:** an earlier LaTeX progress manuscript and October 16 follow-up audit exist outside this repository. The source, complete numerical kernels, and fully benchmarked optimizer are not yet imported.

## Publication policy

1. Preserve the original five arXiv v1 source packages unchanged.
2. Introduce revised drafts alongside those frozen snapshots; distinguish established theorems, conditional results, evidence, and open problems.
3. Make source and compiled PDF available for every active manuscript.
4. Associate each paper with its exact external publication versions. Add hexagonmath.org or other links only after verifying the corresponding public deposit.
5. Keep cross-paper research notes and shared code in dedicated directories, without silently modifying independent submissions.

The repository PDF build checks compilation and provenance, **not** independent mathematical review, novelty, or peer review.
