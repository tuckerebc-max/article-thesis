# Forward-test cases

These are behavioral probes for the skill, not universal writing rules. They are intentionally small and synthetic so a reviewer can check whether the workflow catches predictable failures.

## FT-01 — Correlation cannot carry a causal thesis

**Input:** A survey finds that users who view a dashboard more often report higher confidence. The draft proposes: “Dashboards cause better decisions in schools.”

**Expected behavior:**

- Classify the proposed claim as causal.
- Ask whether the design supports causal inference; a cross-sectional association alone does not.
- Require a warrant and alternative explanations.
- Fail or qualify the causal evidence-fit gate.
- Generate a bounded alternative such as “In this survey, dashboard use is associated with higher reported confidence; whether it improves decision quality remains unresolved.”
- Do not let a dramatic headline repair the evidence defect.

**Failure signal:** The skill accepts “cause” because the source contains a statistically significant association.

## FT-02 — Strong opinion thesis, weak headline

**Input:** A sourced op-ed argues that a state should require schools to report uncertainty around high-stakes assessment results before using them for placement decisions. Proposed headline: “The One Number That Will Save Public Education.”

**Expected behavior:**

- Recognize a possible normative/policy thesis with an explicit Ask.
- Test authority, feasibility, trade-offs, affected groups, and strongest objection.
- Fail the headline for inflated scale, unsupported certainty, and absent specificity.
- Offer a more faithful direction such as “Before schools use assessment results for placement, show how uncertain the number is.”
- Mark the example headline as synthetic and not evidence.

**Failure signal:** The skill rewards the headline because it sounds consequential or clickable.

## FT-03 — Thesis drift across outline and conclusion

**Input:** The working thesis concerns how uncertainty displays change educator interpretation. The outline gradually shifts to whether artificial intelligence should replace assessment systems. The conclusion recommends replacing standardized testing.

**Expected behavior:**

- Snapshot S1, S4, and S6.
- Detect object drift, claim-strength drift, evidence drift, and Ask drift.
- Return `MATERIAL_MISMATCH` or `DRIFT_REQUIRES_DECISION`.
- Require a rewrite, split, or explicit new project.

**Failure signal:** The skill calls this “a stronger conclusion” without comparing the proposition and evidence.

## FT-04 — Structure fit is evidence-dependent

**Input:** A case has a known outcome, and the project’s actual claim is why a small implementation detail produced that outcome. There is no transformation arc and no unresolved mystery.

**Expected behavior:**

- Test Columbo or a direct explanatory structure first.
- Reject Hero’s Journey and Mystery Box as poor fit unless new evidence creates a real transformation or anomaly.
- Stamp the mechanism, evidence, limits, and payoff.

**Failure signal:** The skill selects Prestige or Hero’s Journey merely because the case contains a protagonist.

## FT-05 — Originality cannot be inferred from new wording

**Input:** A writer offers a polished thesis sentence but has not searched the relevant literature or comparable opinion pieces.

**Expected behavior:**

- Separate originality from verbal freshness.
- Mark originality `UNVERIFIED`.
- Recommend corpus/search work before calling the thesis novel.
- Continue testing scope and evidence without pretending the contribution is known.

**Failure signal:** The skill awards a 5 for originality because the sentence sounds distinctive.

## Reviewer checklist

For each forward test, record:

- input version;
- skill version;
- expected behavior;
- observed behavior;
- pass/fail;
- reviewer mode (`INDEPENDENT` or `NON-INDEPENDENT`);
- correction made, if any.

The tests should be rerun when the hard gates, headline checklist, structure crosswalk, drift classifications, or output contracts materially change.

## FT-06 — Polished but interchangeable voice

**Input:** A draft is grammatically clean and balanced but uses generic abstractions, predictable transitions, and no details that identify the writer’s relation to the corpus.

**Expected behavior:**

- Run the voice-versus-polish gate.
- Mark the draft as clear but interchangeable.
- Require a voiceprint, source-derived texture bank, and more particular observations before adoption.
- Do not solve the problem by adding random wit, shorter sentences, or a named-publication voice.

**Failure signal:** The skill calls the piece distinctive because it is smooth.

## FT-07 — New wording mistaken for a field-moving idea

**Input:** A proposed thesis restates the dominant public frame in more forceful language. The writer has not identified an overlooked fact, mechanism, comparison, or reader update.

**Expected behavior:**

- Run the angle lattice and field-moving tests.
- Mark contribution `UNVERIFIED` or fail the contribution gate.
- Ask for the current frame, evidence delta, strongest counter-frame, and before/after reader belief.
- Choose `REVISE` or `DEFER`, not `ADOPT`.

**Failure signal:** The skill awards high originality because the sentence sounds novel.

## FT-08 — Venue fit and author authority are missing

**Input:** A strong 1,400-word essay is proposed for a venue whose current public guidance requests a shorter completed exclusive op-ed. The writer’s conflict and relationship to the issue are undisclosed.

**Expected behavior:**

- Flag length, completion, exclusivity, authority, and conflict/disclosure issues in the editorial brief.
- Separate argument quality from publication fit.
- Recommend narrowing, changing venue, resolving disclosure, or deferring submission.
- Do not promise acceptance or silently treat the venue as interchangeable with another.

**Failure signal:** The skill approves because the argument is compelling.

## FT-09 — Texture is vivid but unsupported

**Input:** A draft opens with a detailed classroom scene that is not in the source corpus and is written as if observed.

**Expected behavior:**

- Fail the provenance/ethics gate.
- Require a sourced or permissioned detail, transparent composite labeling, or a non-fictional opening.
- Do not preserve the scene merely because it improves attention.

**Failure signal:** The skill treats invented specificity as “human texture.”

## FT-10 — Craft range becomes decorative switching

**Input:** Every paragraph alternates between anecdote, statistic, metaphor, question, and historical aside without a change in argumentative job.

**Expected behavior:**

- Identify the dominant craft mode and paragraph jobs.
- Remove modes that do not establish, complicate, evidence, reframe, apply, or close the thesis.
- Preserve range only where it creates meaningful argumentative movement.

**Failure signal:** The skill celebrates variety without testing function, coherence, or voice.

## v0.3.0 reviewer checklist

For each new case, record the skill version, expected behavior, observed behavior, pass/fail, reviewer mode (`INDEPENDENT` or `NON-INDEPENDENT`), and correction made. These cases should be rerun whenever the contribution gate, voiceprint, outlet-fit, anti-slop, or publication-gate references materially change.
