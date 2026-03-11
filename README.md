# Deep Research Skill

A comprehensive research engine that conducts enterprise-grade deep research with multi-source synthesis, citation tracking, and verification.

## Features

- **8-Phase Pipeline:** Scope → Plan → Retrieve → Triangulate → Outline Refinement → Synthesize → Critique → Refine → Package
- **4 Depth Modes:** Quick (2-5 min), Standard (5-10 min), Deep (10-20 min), UltraDeep (20-45 min)
- **Mode Confirmation:** Always asks which mode before starting
- **Modular Output:** Split findings into individual files for easy agent consumption
- **Source Credibility Scoring:** 0-100 scoring based on domain authority, recency, expertise, and bias
- **Anti-Hallucination:** Citation verification via DOI resolution and URL checking
- **Automated Validation:** 8+ quality checks on output

## Installation

Run this command to install the skill into your local environment:

```bash
npx skills add https://github.com/jarodise/deep-research --skill deep-research
```

## Quick Start

Just ask to use deep research — the skill will ask which mode before starting:

```
Use deep research to compare React vs Vue for my project
```

## Output Structure

All output is saved to `{workspace}/{topic}_{date}/`:

```
react_vs_vue_20260311/
├── summary.md              # Executive summary + metadata
├── findings/
│   ├── 01_performance.md   # Individual finding
│   ├── 02_ecosystem.md     # Individual finding
│   └── ...
├── synthesis.md            # Patterns, insights, implications
├── limitations.md          # Gaps, caveats, counterevidence
├── recommendations.md      # Actions and next steps
└── bibliography.md         # All sources with full citations
```

## Architecture

```
deep-research/
├── SKILL.md                    # Main skill definition (~200 lines)
├── reference/
│   ├── methodology.md          # 8-phase pipeline details
│   └── report_generation.md    # Output file templates & writing standards
├── templates/
│   └── report_template.md      # Reference template
├── scripts/
│   ├── validate_report.py      # Quality validation (8 checks)
│   └── verify_citations.py     # Citation verification (DOI + URL + hallucination detection)
└── tests/
    └── fixtures/               # Test reports for validation
```

## Requirements

Python standard library only — no external dependencies.

## Scripts

### validate_report.py

Validates report quality with 8 automated checks:
1. Executive summary length (50-250 words)
2. Required sections present
3. Citations formatted [1], [2], [3]
4. Bibliography matches citations
5. No placeholder text
6. Content truncation detection
7. Word count reasonable
8. Source count check

```bash
python scripts/validate_report.py --report path/to/summary.md
```

### verify_citations.py

Verifies citations aren't fabricated:
- DOI resolution via doi.org
- URL accessibility checking
- Hallucination pattern detection
- Metadata cross-checking

```bash
python scripts/verify_citations.py --report path/to/bibliography.md
python scripts/verify_citations.py --report path/to/bibliography.md --strict
```
