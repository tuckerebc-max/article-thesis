# Article Thesis

Standalone Codex skill package for developing, comparing, and stress-testing article theses for research-based op-eds, guest essays, public-interest articles, and related public-facing writing.

## Release status

**Version:** `0.3.0`  
**Status:** `READY_WITH_CONDITIONS` for private review upload  
**Repository boundary:** upload this folder as the repository root.

The package is designed to be installed as the `article-thesis` skill. Keep `SKILL.md` at repository root and preserve the `agents/`, `references/`, and `scripts/` directories.

## Package contents

- `SKILL.md` ? the portable skill contract, six-stage workflow, boundaries, output contract, and dependency routing.
- `agents/openai.yaml` ? Codex display metadata and invocation configuration.
- `references/` ? thesis tests, field-moving argument guidance, voice and texture guidance, hook/headline craft, narrative crosswalk, output contracts, publication gates, research synthesis, and forward-test records.
- `scripts/validate_skill_package.py` ? dependency-free structural and repository-package validator.
- `.github/workflows/validate.yml` ? no-secret CI check for pushes and pull requests.

## Validate locally

```text
python scripts/validate_skill_package.py
```

The workflow performs the same check on GitHub. It does not install dependencies or publish the package.

## Scope and dependencies

The skill can use the bundled references on its own. When available, it hands off source research, narrative structure, writing craft, anti-slop review, and large-workflow coordination to the named companion skills in `SKILL.md`. If a companion skill is unavailable, the package uses its local contracts and direct narrative fallback; it must not claim that an unavailable dependency ran.

The package does not fabricate sources, findings, quotations, scenes, consent, originality, publication acceptance, or professional/legal determinations. Recheck current facts, outlet rules, conflicts, permissions, and rights before a live submission or public redistribution.

## Conditions before public release

- The recorded forward tests are specification-level and currently labeled `NON-INDEPENDENT`; run a fresh-context review before calling the package stable.
- Confirm current outlet requirements and source status at the publication gate.
- Choose and add an appropriate license before public redistribution; this package intentionally does not assume one.

No GitHub repository creation, remote configuration, or push is performed by the package itself.
