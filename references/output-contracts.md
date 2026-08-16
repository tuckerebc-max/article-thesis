# Output contracts

Use these contracts to keep each run auditable and resumable. All IDs are stable within a project. Do not silently overwrite an earlier decision; add a new version and a change note.

## Status model

```text
NOT_STARTED
SCOPED
CORPUS_BUILT
EXEMPLARS_SCREENED
CANDIDATES_GENERATED
CANDIDATES_TESTED
HOOKS_TESTED
STRUCTURE_STAMPED
DRIFT_AUDITED
REVIEWED
DECIDED
```

Recommended version format: `project-slug.vNN`. Record the date and the person/agent who made each material decision.

## 1. Thesis-development brief

```markdown
# Thesis-development brief

- Project ID:
- Version:
- Status:
- Date:
- Request / deliverable:
- Audience:
- Audience knowledge, resistance, and available action:
- Medium / genre:
- Purpose:
- Length / deadline / constraints:
- Stakes and review requirements:
- Initial topic or question:
- Known source corpus:
- Source authority and citation standard:
- Required dependencies:
- Unknowns / assumptions:
- Non-goals / boundaries:
- Decision needed by the end:
```

## 2. Exemplar cards

Use the fields in [exemplar screening](exemplar-screening.md). Every card needs a source link, access level, reconstruction confidence, and a transfer limitation.

## 3. Thesis candidate matrix

```markdown
# Thesis candidate matrix

- Project ID:
- Version:
- Corpus version:
- Candidate-generation method:
- Hard-gate policy: any failure blocks selection

| ID | Candidate thesis | Type | Scope | Originality | Defensibility | Evidence fit | Audience utility | Narrative potential | Hard gates | Decision |
|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| T-01 |  |  |  |  |  |  |  |  |  |  |

## Gate notes

### T-01

- Claim identity:
- Arguability:
- Scope:
- Warrant:
- Evidence fit:
- Defensibility:
- Audience usefulness:
- Ethical promise:
- Score reasons:
- Strongest objection:
- Response / concession:
- Decision:
```

Scores without reasons are invalid. A score is not evidence and cannot override a failed gate.

## 4. Hook cards

Use the fields in [hook and headline craft](hook-and-headline-craft.md). Each hook must point to its thesis ID, evidence/provenance, promised payoff, and ethical risk.

## 5. Structure stamp

Use the structure-stamp template in [narrative crosswalk](narrative-structure-crosswalk.md). Record top pick, strong alternative, dark horse, and at least one rejected structure when multiple structures were considered.

## 6. Evidence map

```markdown
# Evidence map

- Project ID:
- Version:
- Claim strength policy:

| Claim ID | Claim / subclaim | Type | Source IDs | Support level | Warrant | Qualifier | Counterevidence | Status | Needed action |
|---|---|---|---|---|---|---|---|---|---|
| C-01 |  | descriptive / interpretive / causal / normative / recommendation |  | strong / mixed / weak / absent |  |  |  | VERIFIED / QUALIFIED / UNVERIFIED / CONTESTED |  |

## Source ledger

| Source ID | Citation / link / DOI | Type | Date / access date | Relevant finding | Limitation | Provenance status |
|---|---|---|---|---|---|---|
```

Use `UNVERIFIED` for any material claim whose source, date, or interpretation has not been checked.

## 7. Drift ledger

```markdown
# Drift ledger

- Project ID:
- Version:
- Baseline thesis:
- Drift policy:

| Snapshot | Text or reconstruction | Claim object | Scope | Strength | Evidence in use | Audience / Ask | Change from prior snapshot | Classification | Action |
|---|---|---|---|---|---|---|---|---|---|
| S0 request/topic |  |  |  |  |  |  | baseline |  |  |
| S1 working thesis |  |  |  |  |  |  |  |  |  |
| S2 selected thesis |  |  |  |  |  |  |  |  |  |
| S3 headline/hook |  |  |  |  |  |  |  |  |  |
| S4 outline/titles |  |  |  |  |  |  |  |  |  |
| S5 opening |  |  |  |  |  |  |  |  |  |
| S6 conclusion/Ask |  |  |  |  |  |  |  |  |  |

## Drift verdict

- `STABLE` | `DRIFT_REPAIRABLE` | `DRIFT_REQUIRES_DECISION` | `MATERIAL_MISMATCH`:
- Evidence for verdict:
- Repair or decision:
```

Permitted classifications: `clarification`, `legitimate narrowing`, `legitimate broadening with new evidence`, `rhetorical reframing`, `scope drift`, `claim-strength drift`, `object drift`, `evidence drift`, `audience drift`, `ask drift`, `unresolved`.

## 8. Decision memo

```markdown
# Thesis-development decision

- Project ID:
- Version:
- Status:
- Decision: ADOPT | REVISE | NARROW | SPLIT | DEFER | REJECT
- Confidence: high / medium / low
- Review mode: independent / non-independent

## Selected thesis

- Thesis ID:
- Thesis:
- Claim type:
- Boundary:
- Warrant:
- Evidence fit:
- Strongest objection and response:

## Rejected or deferred alternatives

| ID | Reason not selected | What would make it viable |
|---|---|---|

## Selected public layer

- Hook ID / type:
- Headline direction:
- Headline integrity result:
- Where the promise is paid off:

## Structure

- Narrative Engine arc:
- Communication overlay:
- Structure-stamp result:
- Rejected structure and reason:

## Drift and quality

- Drift verdict:
- Focal cold-read verdict:
- Evidence/research verdict:
- Audience/counterargument verdict:
- Originality status:

## Unresolved gaps and risks

- 

## Next action

- Owner:
- Action:
- Required evidence or decision:
- Due / review point:
```

## Review finding format

For each finding, use:

```text
[ID] [location] [type] [priority P0–P3]
Evidence: ...
Impact: ...
Recommendation: ...
Confidence: high | medium | low
Disposition: accept | revise | reject | defer
```

Types include `evidence`, `scope`, `warrant`, `counterargument`, `originality`, `hook`, `headline`, `structure`, `drift`, `audience`, `ethics`, and `style`.

## Release checklist

- [ ] Source ledger exists and every material claim has a status.
- [ ] At least three materially different thesis candidates were considered, or the reason for fewer is recorded.
- [ ] Hard gates were run before comparative scores.
- [ ] Strongest objection was stated fairly for the selected thesis.
- [ ] Hook and headline are traceable to the thesis and pass integrity tests.
- [ ] Narrative Engine structure is stamped and its rejected alternatives are explained.
- [ ] Drift snapshots include the conclusion/Ask.
- [ ] Cold-read result is independent or explicitly labeled non-independent.
- [ ] Decision and next action are explicit.

## Six-stage op-ed artifacts (v0.3.0)

The revised workflow adds these auditable artifacts. Use the smallest version that preserves the decision; do not write ceremony for its own sake.

### Editorial brief

```markdown
# Editorial brief

- Project / version:
- Target outlet / section:
- Audience and available action:
- Genre / medium:
- Purpose:
- Timely peg / why now:
- Target length / deadline:
- Exclusivity / duplicate-publication status:
- Author relationship, authority, and bio:
- Conflicts / disclosures:
- Source and citation standard:
- Legal / ethical sensitivities:
- Non-goals:
- Provisional problem statement:
- Decision needed by the end:
```

### Corpus map

```markdown
# Corpus map

- Project / version:
- Search boundary and stopping rule:
- Field’s current frame:
- Consensus / disputes / absences:
- Candidate contribution:

## Evidence ledger

| Source ID | Citation / link / date | Type | Claim supported | Population / setting | Limitation | Verification |
|---|---|---|---|---|---|---|

## Texture bank

| Texture ID | Detail | Provenance | Function | Scope / limitation | Planned use |
|---|---|---|---|---|---|
```

### Angle lattice

```markdown
# Angle lattice

- Current public/field frame:
- Overlooked fact, population, cost, or contradiction:
- Reconnection or mechanism:
- New consequence:
- Writer authority / relationship:
- Reader update:
- Ask:

| Candidate | Contribution type | Evidence delta | Strongest counter-frame | Reader before/after | Originality status | Decision |
|---|---|---|---|---|---|---|
```

### Voiceprint and op-ed architecture

Use the templates in [voiceprint and corpus texture](voiceprint-and-corpus-texture.md) and [field-moving argument](field-moving-argument.md). The architecture must record the opening promise, early thesis, evidence ladder, counterargument pressure, turn/reframe, Ask, close, headline directions, and Narrative Engine arc/overlay.

### Publication gate

Use the record in [revision and publication gates](revision-and-publication-gates.md). It must state whether the reviewer was independent and must not call a same-agent self-check independent.

## Additional release statuses

Projects using v0.3.0 may add `BRIEFED`, `FIELD_MAPPED`, `VOICEPRINTED`, `ARCHITECTURE_BUILT`, and `PUBLICATION_GATED` between the existing statuses.
