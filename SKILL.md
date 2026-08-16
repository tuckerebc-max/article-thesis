---
name: article-thesis
description: Develop, compare, and stress-test article theses for research-based op-eds, guest essays, public-interest articles, and other public-facing writing. Use when an article needs a field-moving controlling claim, distinctive source-derived voice, evidence-grounded hooks and headlines, narrative architecture, thesis-drift detection, or a clear contrast with a journal article thesis or LinkedIn post thesis.
---

# Article Thesis

Version 0.3.0 - article-focused GitHub delivery package.

## Purpose and editorial bar

This skill is a six-stage decision system for turning a topic, question, corpus, or rough draft into a defensible public argument. Its primary public-facing mode is the research-based op-ed or guest essay: clear enough to enter quickly, original enough to change the conversation, grounded enough to withstand scrutiny, and alive enough to be remembered. It also supports academic, policy, explanatory, and hybrid work.

The standard is not "polished prose." A strong result should have:

- a real public or intellectual claim, not a topic wearing a thesis costume;
- a contribution that changes what an informed reader sees, connects, questions, or does;
- evidence whose provenance, limitations, and warrant are visible;
- a voice that comes from the writer's relation to the material, not from generic "op-ed voice" or imitation of a named writer or publication;
- a range of craft chosen for function: scene, explanation, history, comparison, data, testimony, moral pressure, or systems thinking where each earns its place;
- counterargument handled as pressure on the idea, not as a ritual paragraph;
- a hook, headline, structure, and closing that make the same honest promise;
- language with texture, precision, rhythm, and restraint; and
- an anti-slop result: specific, non-interchangeable, non-canned, and free of invented human detail.

Use editorial expectations associated with target publications as high-level benchmarks for clarity, freshness, evidence, reader value, and editorial discipline. Do not imitate a living writer or reproduce a publication's proprietary house style. See [outlet fit and editorial bar](references/outlet-fit-and-editorial-bar.md). No workflow can guarantee acceptance.

The terms must stay separate:

| Element | Job | Failure when confused with another element |
|---|---|---|
| Thesis | The contestable proposition the piece is built to establish | Topic, summary, slogan, fact, or unsupported preference |
| Contribution | What the piece adds relative to the screened field/corpus | New wording mistaken for new thinking |
| Warrant | Why the evidence supports the thesis | Hidden assumption or rhetorical leap |
| Evidence fit | Whether the available evidence supports the claim at its actual strength and scope | Citation decoration or causal overreach |
| Voiceprint | The writer's source-grounded stance, diction, rhythm, vantage, and ethical signature | Generic polish or writer imitation |
| Texture | Concrete, attributable particulars that make the argument inhabited and credible | Decorative detail or fabricated scene |
| Hook | The entry point that earns attention and creates a reason to continue | Sensational promise, thesis substitute, or clickbait |
| Headline/title | The compact public promise of the piece | Label, teaser that withholds the point, or claim stronger than the body |
| Narrative structure | The sequence that makes the thesis intelligible and consequential | Template chosen for drama rather than fit |
| Ask/implication | What the audience should understand, consider, decide, or do | Conclusion smuggled in without support |

## Operating contract

Every run should preserve these fields, even when the user provides only a rough topic:

- `editorial_brief`: outlet or venue, audience, purpose, format, length, peg, timing, author relation, exclusivity, conflicts, and constraints;
- `source_corpus`: source IDs, dates, provenance, evidence type, claims supported, limitations, and known gaps;
- `field_map`: current conversation, consensus, disputes, blind spots, absent voices, and the piece's possible contribution;
- `texture_bank`: source-traceable people, places, objects, language, numbers, contradictions, moments, and human consequences;
- `thesis_candidates`: 3-7 materially different candidates when the material permits;
- `evidence_map`: claim-to-source support, warrant, qualifier, counterevidence, and unresolved status;
- `voiceprint`: vantage, authority, stakes, diction, rhythm, tonal range, personal-material boundaries, and anti-slop exclusions;
- `hook_cards`: source-grounded openings and their promises/payoffs;
- `headline_set`: multiple honest variants tested out of context;
- `structure_stamp`: Narrative Engine arc/overlay choice and beat-level fit;
- `architecture`: opening promise, thesis placement, evidence ladder, counterargument pressure, turn, implication, and close;
- `drift_ledger`: snapshots from initial idea through conclusion;
- `review_record`: independent or non-independent findings, unresolved risks, and corrections;
- `decision`: `ADOPT`, `REVISE`, `NARROW`, `SPLIT`, `DEFER`, or `REJECT`, with rationale and next action.

If a field is missing, mark it `UNKNOWN` or `UNVERIFIED`; do not invent it. If a claim needs facts that are not in the corpus, narrow the claim, label treatment hypothetical, or recommend research before drafting.

## Workflow

The six stages below are the required operating spine. They may be repeated, but they should not be silently skipped. Keep intermediate artifacts versioned so a later draft cannot quietly replace the original decision.

### Stage 1 - Commission and editorial brief

Create `editorial-brief.md` before generating a serious thesis or prose. Establish:

- target reader, what that reader knows, resists, feels, and can do;
- venue/section and genre: academic, op-ed, guest essay, analysis, column, report, or hybrid;
- purpose: explain, interpret, evaluate, persuade, recommend, decide, or investigate;
- timely peg, public stake, and why this piece now;
- target length, deadline, exclusivity/duplicate-publication constraints, and submission rules;
- author's relationship to the issue, relevant authority, personal material available, and conflicts or disclosures;
- source standard, citation/link expectation, legal/ethical sensitivities, and non-goals;
- provisional one-sentence problem statement and what would count as a useful result.

Use current outlet guidance when a real submission is intended. Word counts, exclusivity, contact requirements, and contributor rules change; stamp them `[as of: YYYY-MM-DD]` and verify again before submission. A piece may be excellent and still be wrong for a venue because its length, peg, evidence, audience, or author authority does not fit.

Ask only high-impact questions. If the user has not answered one, make a provisional assumption and label it. Do not treat a request for "a strong angle" as permission to assert an unverified fact.

### Stage 2 - Corpus, field, and texture map

Build `corpus-map.md` before deciding that an idea is original. Use `$deep-research` when the source base is incomplete, current, disputed, or consequential. Prefer primary, official, peer-reviewed, and directly observed evidence; cite the source near the claim in the final work.

Create three linked maps:

1. **Evidence ledger:** source, date, provenance, claim supported, population/setting, limitation, and verification state.
2. **Conversation map:** what the field/public conversation says, assumes, disputes, neglects, and cannot yet explain.
3. **Texture bank:** concrete, source-traceable particulars that can carry human meaning without being used as proof beyond their scope.

For each source distinguish `DIRECT`, `PARAPHRASE`, `INFERRED`, `HYPOTHETICAL`, and `NEEDS-SOURCE`. Screen for selection bias, stale information, missing counterevidence, incompatible populations or constructs, correlation/causation confusion, overgeneralization from a case, and authority that does not match the claim.

Study exemplars as analyzable objects, not idols. For academic and opinion exemplars, reconstruct audience, thesis, warrant, evidence, counterargument, opening, turn, payoff, close, and transfer limitation. Include successful examples, a failure/counterexample, and at least one example chosen for argument or evidence quality rather than fame. See [exemplar screening](references/exemplar-screening.md).

A texture detail earns inclusion only when its provenance and function are clear. Useful texture may include a person's exact words, a place, an object, a time marker, a contradiction, a measured number, a procedural detail, a source's unusual phrase, or a consequence visible at human scale. Never manufacture a scene, composite a person without disclosure, or use a vivid anecdote as population-level evidence.

### Stage 3 - Thesis and angle laboratory

Create `angle-lattice.md` and `thesis-candidate-matrix.md`. Generate 3-7 candidates that differ in claim, mechanism, object, scope, consequence, or decision-not cosmetic rewrites. For each candidate state:

> In **[bounded context]**, **[object/process]** is best understood as or should be **[contestable claim]** because **[mechanism or warrant]**; the strongest evidence is **[evidence base]**, the main limitation is **[boundary]**, and this matters because **[stake/implication]**.

Use the form as a diagnostic, not a mandatory sentence shape. Candidate types may include interpretive, causal/explanatory, comparative, evaluative, methodological, normative/policy, design/recommendation, or opinion diagnosis plus feasible action. Academic work may need a multi-sentence thesis, hypothesis, or research question with a provisional answer.

Run the **field-moving test**. A candidate earns originality only if it offers a new interpretation, connection, mechanism, comparison, synthesis, application, question, or decision relative to the screened corpus. Ask:

- What is the current frame or conventional explanation?
- What does this candidate see that the current frame misses?
- What evidence makes the difference visible?
- What reasonable reader would think, ask, or do differently if persuaded?
- Is the contribution genuinely new, or only newly phrased?

Mark originality `UNVERIFIED` when the search is incomplete. A memorable sentence is not evidence of a new idea.

For every candidate, write the strongest fair objection before scoring it. Decide whether to concede, narrow, revise, rebut, or leave unresolved. Avoid pro forma "some might say" paragraphs; counterargument should exert pressure on the claim's design.

Run hard gates before scores:

| Gate | Pass condition | Failure response |
|---|---|---|
| Claim identity | A reader can state what the writer wants accepted | Rewrite as a proposition |
| Field-moving contribution | The candidate adds a traceable interpretation, connection, mechanism, application, or decision | Research, distinguish contribution, or reject |
| Arguability | A thoughtful reader could disagree for substantive reasons | Add a real tension or decision |
| Scope | Object, setting, time, population/construct, and strength are bounded | Narrow, qualify, or split |
| Warrant | The reasoning bridge from evidence to claim is visible | State, test, or weaken the warrant |
| Evidence fit | Sources support the claim's kind and strength; contrary evidence is not hidden | Research, qualify, change claim, or defer |
| Defensibility | The strongest objection can be answered or incorporated fairly | Revise or reject |
| Audience usefulness | This audience has a reason to care, understand, or act | Reframe stakes or audience |
| Ethical promise | The argument can be made without fabrication, material deception, or coercive pressure | Replace the entry point or claim |

Only candidates that pass all hard gates receive comparative scores. Score 1-5 for scope fit, contribution, defensibility, evidence fit, explanatory power, audience utility, voice potential, and narrative potential. Record reasons. A high total never overrides a failed gate.

### Stage 4 - Voiceprint and texture architecture

Create `voiceprint.md`. Voice is not a decorative finish applied after research. It is the particular way this writer sees, values, notices, doubts, names, and organizes the material. Derive it from the author's relation to the subject and the corpus; do not imitate a named writer, newspaper, magazine, or columnist.

Record:

- vantage and authority: where the writer is standing and why the reader should trust that position;
- felt stakes and ethical center: what the writer refuses to trivialize or fake;
- intellectual posture: diagnostic, skeptical, hopeful, impatient, wry, elegiac, practical, contrarian, or another evidenced stance;
- diction and rhythm: plain/technical balance, sentence length range, paragraph movement, use of first person, and tolerance for fragments;
- image ecology: recurring concrete objects, places, metaphors, or institutional language that belong to this subject;
- tonal range: where the piece may move from explanation to scene, irony, grief, anger, or invitation, and what earns each movement;
- permissible personal material and disclosure boundary;
- phrases, patterns, clichés, abstractions, and "AI-sounding" habits to avoid;
- 2-4 distinctive phrases or passages worth protecting because they are earned by the corpus, not because they sound pretty.

Select a dominant craft mode and, if useful, one supporting mode: scene/portrait, explanatory/causal, moral/policy, historical, comparative, systems, personal testimony, data-led, reversal, or reported case. Vary modes only when the argument changes job. Do not decorate every paragraph with a new flourish.

Run the **voice-versus-polish gate**:

- clear but interchangeable = fail;
- vivid but ungrounded = fail;
- distinctive, precise, evidence-linked, and ethically bounded = pass.

Run the anti-slop check in [op-ed craft and anti-slop](references/op-ed-craft-and-anti-slop.md). The draft must not be a generic professional voice that could be pasted into another writer's piece unchanged.

### Stage 5 - Hook, headline, narrative, and draft architecture

Create `op-ed-architecture.md` before drafting full prose. Make the argument choreography explicit:

`opening promise -> early thesis -> evidence ladder -> pressure/counterargument -> real turn or reframe -> implication/Ask -> earned close`

The thesis should become findable early in a public argument, even if the opening begins with a scene, image, question, or contradiction. The close should deepen or apply the thesis, not introduce a larger unsupported claim.

Develop hook cards after the candidate logic is visible, while allowing early hook attempts to diagnose the genuine interest. A hook must reveal a real tension, consequence, question, person/case, pattern, image, decision, or supported surprise and must have a traceable payoff. Do not use a fabricated scene, unsupported statistic, or hidden premise.

Test at least three headline directions: explanatory, tension/contrast, and human/concrete entry point. Treat a headline as a one-idea public promise. It must be accurate without the article, image, brand, or context; clear on a fast screen; specific about subject and payoff; proportionate to evidence; and tonally matched. A clever headline that misstates the thesis fails.

Use `$narrative-engine` as the structural authority. Record `One Thing`, `Ask`, `Through-Line`, `Boundary`, audience facts, evidence standard, and risks. Evaluate arcs and communication overlays for `Context Fit`, `Focal Fit`, and `Evidence Fit` on a 1-5 scale. Disqualify any structure with Focal or Evidence Fit below 3. Use no more than one narrative arc plus one communication overlay. Choose a dramatic structure only when there is a genuine anomaly, transformation, unresolved question, or consequence; otherwise use direct explanation, comparison, or argument.

Return `TOP PICK`, `STRONG ALTERNATIVE`, `DARK HORSE`, and at least one `REJECTED` option when multiple structures were considered. Stamp the skeleton before drafting: every protected beat must advance, complicate, evidence, or properly qualify the thesis. If no structure passes, use `Answer -> Why -> Evidence -> Limits/Risks -> Action/Next question` or narrow/split the project.

### Stage 6 - Revision, cold read, and publication gate

Revise in this order: argument and scope; evidence and attribution; architecture and paragraph jobs; voice and texture; sentence-level craft; headline/opening/close; anti-slop; submission fit. See [revision and publication gates](references/revision-and-publication-gates.md).

Capture drift snapshots:

`S0 topic/request -> S1 working thesis -> S2 selected thesis -> S3 headline/hook -> S4 outline/section titles -> S5 opening -> S6 conclusion/Ask`.

Compare proposition, object, scope, mechanism, strength, evidence, counterargument, audience, and Ask. Classify changes as `clarification`, `legitimate narrowing`, `legitimate broadening with new evidence`, `rhetorical reframing`, `scope drift`, `claim-strength drift`, `object drift`, `evidence drift`, `audience drift`, `ask drift`, or `unresolved`.

Use a fresh-context cold read when possible: the reviewer states the piece's point in one sentence before reading the brief. Label a same-agent review `NON-INDEPENDENT`. Run the headline-to-body, section-title, conclusion, evidence, voice, texture, and outlet-fit tests. Any unresolved material claim, invented detail, indistinct voice, unsupported escalation, or wrong-venue constraint blocks `ADOPT`.

The final package should include `publication-gate.md` and `decision.md`. A good result is not "the prose sounds strong." It is "the argument is bounded, field-moving, source-traceable, texturally inhabited, voice-specific, structurally earned, and stable across the piece."

## Decision policy

Use:

- `ADOPT`: hard gates pass; remaining edits are bounded and non-structural;
- `REVISE`: the idea is viable but argument, voice, evidence, or architecture needs work;
- `NARROW`: the claim outruns the evidence or venue;
- `SPLIT`: two legitimate theses are competing;
- `DEFER`: material research, authority, timing, or decision input is missing;
- `REJECT`: the contribution, evidence fit, ethics, or audience value cannot be repaired responsibly.

Do not award "best-in-class" status from prose quality alone. Record confidence, unresolved risks, and the next action.

## Dependency routing

- `$narrative-engine`: source inventory, focal statement, arc/overlay selection, skeleton stamp, provenance, and cold-read/evidence gates.
- `$writing-craft-armature`: controlling proposition, section service, subtraction, because-joints, and earned conclusion.
- `$writing-craft`: attention sequence, actor/action, cohesion, rhythm, end-stress, concision, and read-aloud revision.
- `$anti-ai-slop-writing`: banned-phrase scan, cadence variation, specificity, anti-template checks, and preservation of distinctive phrasing.
- `$deep-research`: source strategy, primary-source preference, uncertainty, adversarial comparison, and citation verification.
- `$agent-workflow-designer`: bounded roles, checkpoints, canonical outputs, and exception handling for large projects.
- `hooks skill`: optional downstream dependency for additional hook ideation; this skill's hook cards remain the contract.

When a named dependency is unavailable, continue with the bundled contracts and the direct fallback in [narrative crosswalk](references/narrative-structure-crosswalk.md). Do not imply that a dependency ran or invent its outputs. Dependency handoffs cannot override evidence, authorship, safety, or currentness boundaries.

## Research basis

The bundled references synthesize institutional thesis guidance, Toulmin argument design, newsroom/editorial submission guidance, headline research, narrative research, local craft skills, and outlet-specific public guidance. They are design inputs, not a substitute for the linked sources. Refresh current or disputed claims during each project.

See [research synthesis](references/research-synthesis.md), [outlet fit and editorial bar](references/outlet-fit-and-editorial-bar.md), [field-moving argument](references/field-moving-argument.md), [voiceprint and corpus texture](references/voiceprint-and-corpus-texture.md), [op-ed craft and anti-slop](references/op-ed-craft-and-anti-slop.md), [revision and publication gates](references/revision-and-publication-gates.md), [headline and hook craft](references/hook-and-headline-craft.md), [thesis tests](references/thesis-taxonomy-and-tests.md), [narrative crosswalk](references/narrative-structure-crosswalk.md), [exemplar screening](references/exemplar-screening.md), [output contracts](references/output-contracts.md), [forward tests](references/forward-test-cases.md), and [forward-test results](references/forward-test-results.md).

## Proposed project metadata

- Proposed Linear destination: `Project: Writing Craft / Editorial Skills`
- Candidate issue: `Develop thesis, hook, and narrative-structure selection workflow`
- Decision in this package: `ADOPT` version 0.3.0 for internal testing and forward-testing; retain Linear/GitHub actions as metadata only unless separately authorized.
