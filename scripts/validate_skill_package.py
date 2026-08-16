#!/usr/bin/env python3
"""Validate the article-thesis skill package without network access."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_REFERENCES = {
    "references/research-synthesis.md",
    "references/thesis-taxonomy-and-tests.md",
    "references/hook-and-headline-craft.md",
    "references/narrative-structure-crosswalk.md",
    "references/exemplar-screening.md",
    "references/output-contracts.md",
    "references/outlet-fit-and-editorial-bar.md",
    "references/field-moving-argument.md",
    "references/voiceprint-and-corpus-texture.md",
    "references/op-ed-craft-and-anti-slop.md",
    "references/forward-test-cases.md",
    "references/forward-test-results.md",
    "references/revision-and-publication-gates.md",
}
REQUIRED_REPOSITORY_FILES = {
    "README.md",
    ".gitignore",
    ".gitattributes",
    ".github/workflows/validate.yml",
}



def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skill-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Skill directory to validate (default: parent of this script)",
    )
    args = parser.parse_args()
    skill_dir = args.skill_dir.resolve()
    errors: list[str] = []

    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        fail("missing SKILL.md", errors)
    else:
        text = skill_file.read_text(encoding="utf-8-sig")
        lines = text.splitlines()
        if len(lines) > 500:
            fail(f"SKILL.md has {len(lines)} lines; keep it at or below 500", errors)
        if not text.startswith("---\n"):
            fail("SKILL.md does not start with YAML frontmatter", errors)
        else:
            end = text.find("\n---\n", 4)
            if end < 0:
                fail("SKILL.md frontmatter is not closed", errors)
            else:
                frontmatter = text[4:end]
                for line in frontmatter.splitlines():
                    if line.strip() and not line.startswith(("name:", "description:")):
                        fail("SKILL.md frontmatter may contain only name and description", errors)
                name = re.search(r"^name:\s*([^\n]+)$", frontmatter, re.MULTILINE)
                description = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
                if not name or name.group(1).strip() != "article-thesis":
                    fail("frontmatter name must be article-thesis", errors)
                if skill_dir.name != "article-thesis":
                    fail("skill folder must be named article-thesis", errors)
                if not description or len(description.group(1).strip()) < 80:
                    fail("frontmatter description is missing or too short", errors)
                if description and "Use when" not in description.group(1):
                    fail("frontmatter description must include explicit trigger guidance", errors)
        if "TODO" in text:
            fail("SKILL.md still contains TODO text", errors)
        for ref in re.findall(r"\]\(references/([^\)]+)\)", text):
            if not (skill_dir / "references" / ref).is_file():
                fail(f"linked reference does not exist: references/{ref}", errors)
        for heading in (
            "## Purpose and editorial bar",
            "## Operating contract",
            "## Workflow",
            "### Stage 1 - Commission and editorial brief",
            "### Stage 2 - Corpus, field, and texture map",
            "### Stage 3 - Thesis and angle laboratory",
            "### Stage 4 - Voiceprint and texture architecture",
            "### Stage 5 - Hook, headline, narrative, and draft architecture",
            "### Stage 6 - Revision, cold read, and publication gate",
            "## Decision policy",
            "## Dependency routing",
            "## Research basis",
        ):
            if heading not in text:
                fail(f"SKILL.md missing required heading: {heading}", errors)
        for phrase in (
            "field-moving test",
            "voice-versus-polish gate",
            "anti-slop",
            "publication gate",
        ):
            if phrase not in text.lower():
                fail(f"SKILL.md missing required quality concept: {phrase}", errors)

    yaml_file = skill_dir / "agents" / "openai.yaml"
    if not yaml_file.is_file():
        fail("missing agents/openai.yaml", errors)
    else:
        yaml_text = yaml_file.read_text(encoding="utf-8-sig")
        for required in (
            "display_name:",
            "short_description:",
            "default_prompt:",
            "$article-thesis",
            "allow_implicit_invocation: true",
        ):
            if required not in yaml_text:
                fail(f"agents/openai.yaml missing {required}", errors)

    for rel in sorted(REQUIRED_REPOSITORY_FILES):
        path = skill_dir / rel
        if not path.is_file():
            fail(f"missing repository file: {rel}", errors)

    readme = skill_dir / "README.md"
    if readme.is_file():
        readme_text = readme.read_text(encoding="utf-8-sig")
        for required in ("SKILL.md", "agents/openai.yaml", "scripts/validate_skill_package.py"):
            if required not in readme_text:
                fail(f"README.md missing repository guidance for {required}", errors)

    workflow = skill_dir / ".github" / "workflows" / "validate.yml"
    if workflow.is_file() and "scripts/validate_skill_package.py" not in workflow.read_text(encoding="utf-8-sig"):
        fail(".github/workflows/validate.yml must run scripts/validate_skill_package.py", errors)

    for rel in sorted(REQUIRED_REFERENCES):
        path = skill_dir / rel
        if not path.is_file():
            fail(f"missing required reference: {rel}", errors)
        elif not path.read_text(encoding="utf-8-sig").strip():
            fail(f"reference is empty: {rel}", errors)

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    print(f"Skill package: {skill_dir}")
    print(f"References checked: {len(REQUIRED_REFERENCES)}")
    print("Frontmatter, six-stage architecture, quality concepts, interface metadata, links, headings, and TODO scan passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
