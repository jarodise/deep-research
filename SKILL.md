---
name: deep-research
description: Conduct enterprise-grade research with multi-source synthesis, citation tracking, and verification. You MUST use this skill whenever the user asks for a "deep research", "comprehensive analysis", "market research", "literature review", wants to compare complex technologies (e.g., "compare X vs Y"), or requests any investigation that requires looking up multiple sources. Trigger this skill even if they don't explicitly say "deep research", as long as the question requires synthesizing factual information from the web. Do NOT use for simple lookups, debugging, or coding.

# Deep Research

## Core Purpose

Deliver citation-backed, verified research through an 8-phase pipeline (Scope → Plan → Retrieve → Triangulate → Outline Refinement → Synthesize → Critique → Refine → Package) with source credibility scoring and modular file output optimized for agent consumption.

---

## Step 1: Confirm Mode with User (ALWAYS DO THIS FIRST)

Before starting any research, present the mode options and ask the user to choose:

```
I'll conduct deep research on this topic. Which mode would you like?

| Mode         | Phases | Time     | Best For                          |
|-------------|--------|----------|-----------------------------------|
| **Quick**    | 3      | 2-5 min  | Initial exploration, broad overview |
| **Standard** | 6      | 5-10 min | Most research needs (recommended)  |
| **Deep**     | 8      | 10-20 min| Important decisions, thorough verification |
| **UltraDeep**| 8+     | 20-45 min| Critical analysis, maximum rigor   |
```

**Wait for user response before proceeding.** Do not assume a mode.

---

## Step 2: Execute Research Phases

### All modes execute:
- **Phase 1: SCOPE** — Define boundaries ([methodology](./reference/methodology.md#phase-1-scope))
- **Phase 3: RETRIEVE** — Search execution (5-10 searches) ([methodology](./reference/methodology.md#phase-3-retrieve---parallel-information-gathering))
- **Phase 8: PACKAGE** — Generate output files ([report generation](./reference/report_generation.md))

### Standard/Deep/UltraDeep also execute:
- **Phase 2: PLAN** — Strategy formulation
- **Phase 4: TRIANGULATE** — Verify 3+ sources per claim
- **Phase 4.5: OUTLINE REFINEMENT** — Adapt structure based on evidence ([methodology](./reference/methodology.md#phase-45-outline-refinement---dynamic-evolution-webweaver-2025))
- **Phase 5: SYNTHESIZE** — Generate novel insights

### Deep/UltraDeep also execute:
- **Phase 6: CRITIQUE** — Red-team analysis
- **Phase 7: REFINE** — Address gaps

**Load [methodology](./reference/methodology.md) sections on-demand for current phase only. Do not preload all content.**

---

## Step 3: Search Execution (Phase 3)

**Launch ALL searches in a single message with multiple tool calls — NOT sequentially.**

Decompose the query into 5-10 independent search angles:
1. Core topic (semantic search)
2. Technical details (keyword search)
3. Recent developments (date-filtered 2024-2025)
4. Academic sources (domain-specific)
5. Alternative perspectives / criticisms
6. Statistical data / benchmarks
7. Industry analysis
8. Limitations and failure modes

**Choose ONE search tool per session:**
- **WebSearch** (built-in): `WebSearch(query="...")`
- **Exa MCP** (if available): `mcp__Exa__exa_search(query="...", type="neural", num_results=10)`

**Never mix parameter styles between tools — causes errors.**

**Quality gate — proceed to next phase when FIRST threshold reached:**
- Quick: 10+ sources, avg credibility >60
- Standard: 15+ sources, avg credibility >60
- Deep: 25+ sources, avg credibility >70
- UltraDeep: 30+ sources, avg credibility >75

---

## Step 4: Write Output Files

**CRITICAL: Output goes under the current workspace, NOT ~/Documents.**

### Output Structure

```
{workspace}/{topic_slug}_{YYYYMMDD}/
├── summary.md              # Executive summary + metadata
├── findings/
│   ├── 01_{finding_title}.md
│   ├── 02_{finding_title}.md
│   └── ...                 # One file per major finding
├── synthesis.md            # Patterns, insights, implications
├── limitations.md          # Gaps, caveats, counterevidence
├── recommendations.md      # Actions and next steps
└── bibliography.md         # All sources with full citations
```

**Why split files:** Individual findings are easier for agents to read, reference, and process than a monolithic report. Each file is self-contained with its own citations.

**Load [report generation instructions](./reference/report_generation.md) for detailed templates and writing standards.**

---

## Step 5: Validate Output

Run validation after generating all files:

```bash
python scripts/validate_report.py --report {path_to_summary.md}
```

```bash
python scripts/verify_citations.py --report {path_to_bibliography.md}
```

**If validation fails:**
- Attempt 1: Auto-fix formatting/links
- Attempt 2: Manual review + correction
- After 2 failures: STOP → Report issues → Ask user

---

## Anti-Hallucination Protocol

- **Source grounding**: Every factual claim MUST cite a specific source [N]
- **Clear boundaries**: Distinguish FACTS (from sources) from SYNTHESIS (your analysis)
- **Explicit markers**: Use "According to [1]..." or "[1] reports..." for factual statements
- **No speculation without labeling**: Mark inferences as "This suggests..." not "Research shows..."
- **Verify before citing**: If unsure whether source says X, do NOT fabricate citation
- **When uncertain**: Say "No sources found for X" rather than inventing references

---

## Writing Standards

- **Precision**: Every word deliberately chosen — "reduced mortality 23%" not "significantly improved"
- **Economy**: No fluff, no unnecessary modifiers
- **Clarity**: Exact numbers in sentences — "5 RCTs (n=1,847)" not "several studies"
- **Directness**: State findings without embellishment
- **Prose-first**: Use bullets only for distinct lists. ≥80% flowing prose
- **Citation density**: Major claims cited in same sentence

**Source Attribution:**
- ✅ GOOD: "Mortality decreased 23% (p<0.01) in the treatment group [1]."
- ❌ BAD: "Studies show mortality improved significantly."
- ✅ GOOD: "Smith et al. (2024) found..." [1]
- ❌ BAD: "Research suggests...", "Experts believe..."

---

## Source Credibility Scoring

Score each source 0-100 based on:

| Factor | Weight | High Score | Low Score |
|--------|--------|-----------|-----------|
| Domain authority | 35% | .gov, arxiv.org, nature.com | blogspot.com, personal sites |
| Recency | 20% | <3 months: 100, <1yr: 85 | >5 years: 30 |
| Expertise | 25% | Academic, official docs | Generic blogs |
| Bias/neutrality | 20% | Balanced language, peer-reviewed | Sensational titles |

**Recommendations:**
- ≥80: High trust
- 60-79: Moderate trust
- 40-59: Low trust — verify claims
- <40: Verify independently before citing

---

## Quality Standards

Every research output must have:
- 10+ sources (document if fewer)
- 3+ sources per major claim
- Executive summary <250 words
- Full citations with URLs
- Credibility assessment
- Limitations section
- No placeholder text (TBD, TODO, FIXME)

---

## Error Handling

**Stop immediately if:**
- 2 validation failures on same error → Pause, report, ask user
- <5 sources after exhaustive search → Report limitation, ask user
- User interrupts/changes scope → Confirm new direction

**Graceful degradation:**
- 5-10 sources → Note in limitations, proceed with extra verification
- Time constraint reached → Package partial results, document gaps

---

## When to Use / NOT Use

**Use when:**
- Comprehensive analysis (10+ sources needed)
- Comparing technologies/approaches/strategies
- State-of-the-art reviews
- Multi-perspective investigation
- Market/trend analysis

**Do NOT use:**
- Simple lookups (use web search directly)
- Debugging (use standard tools)
- Questions answerable with 1-2 searches
- Time-sensitive quick answers

---

## Scripts (Python stdlib only)

**Location:** `./scripts/`

- **validate_report.py** — Quality validation (8 checks)
- **verify_citations.py** — Citation verification (DOI + URL + hallucination detection)

**No external dependencies required.**

---

## Progressive References (Load On-Demand)

- [Complete Methodology](./reference/methodology.md) — 8-phase details
- [Report Generation](./reference/report_generation.md) — Output file templates and standards

**Load files on-demand for current phase only. Do not preload all content.**
