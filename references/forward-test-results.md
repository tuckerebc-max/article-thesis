# Forward-test results

This record retains the baseline review and the v0.3.0 revision review. The baseline is historical; the v0.3.0 section is the current package review.

## Baseline v0.1.0 review

- Skill version: 0.1.0
- Review date: 2026-08-14
- Review mode: `NON-INDEPENDENT` self-review; no fresh-context subagent was available in this task
- Method: read the core workflow and test cases independently from the source research notes, then checked each expected behavior against the written gates and contracts

| Test | Result | Observed behavior |
|---|---|---|
| FT-01 correlation-to-causal overreach | PASS | The workflow classifies causal claims, requires a mechanism/warrant, maps claim type to evidence fit, and blocks a candidate when the design cannot carry causal strength. |
| FT-02 inflated opinion headline | PASS | The opinion pathway requires an Ask, timing, audience, evidence, feasibility, trade-offs, and objection handling; the headline gate blocks unsupported scale and certainty. |
| FT-03 thesis drift | PASS | S0–S6 snapshots and classifications include object, scope, strength, evidence, audience, and Ask drift; material mismatch requires a decision. |
| FT-04 structure mismatch | PASS | The crosswalk routes known-outcome mechanism work to Columbo/direct explanation and rejects dramatic arcs without a genuine turn, anomaly, or transformation. |
| FT-05 false originality | PASS | Originality is defined relative to the screened corpus and must be marked `UNVERIFIED` when the search is incomplete. |

## Residual limitation

This is a specification-level forward test, not an independent user trial. Before calling the skill stable, run the five cases with a fresh-context reviewer or another writer and record disagreement, false positives, and missed drift. Prioritize testing on an academic paper, an evidence-based op-ed, and a project with a changing brief.

## v0.3.0 revision review

- Skill version: 0.3.0
- Review date: 2026-08-14
- Review mode: `NON-INDEPENDENT` specification review; no fresh-context reviewer was available in this task
- Method: checked the six-stage workflow, new references, output contracts, and forward-test cases against the requested op-ed quality bar and the benchmark sources

| Test | Result | Observed behavior |
|---|---|---|
| FT-06 polished but interchangeable voice | PASS | The voice-versus-polish gate, voiceprint, paste test, and source-return test block generic smoothness from counting as distinctiveness. |
| FT-07 new wording mistaken for movement | PASS | The angle lattice requires a current frame, evidence delta, counter-frame, reader update, and originality status before adoption. |
| FT-08 outlet fit and authority missing | PASS | The editorial brief and publication gate separate argument quality from current length, exclusivity, authority, conflict, and venue-fit requirements. |
| FT-09 vivid unsupported texture | PASS | Provenance and ethics gates reject invented or undisclosed scenes and require sourced, permissioned, or transparently labeled material. |
| FT-10 decorative craft switching | PASS | The craft-mode palette and paragraph-job test preserve variety only when it changes argumentative function. |

## Residual limitation

This remains a specification-level review rather than an independent user trial. Before calling v0.3.0 stable, run the ten cases with a fresh-context reviewer or another writer and record disagreements, false positives, missed drift, and whether the voice gate can distinguish distinctive writing from merely unusual writing. Prioritize a research-based education op-ed, a general-interest opinion essay, and an academic argument with a changing brief.
