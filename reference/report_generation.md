# Report Generation — Phase 8 Instructions

## Output Location

Save all output under the current workspace:

```
{workspace}/{topic_slug}_{YYYYMMDD}/
```

- Extract a clean topic slug from the research question (lowercase, underscores, no special chars)
- Examples:
  - "compare React vs Vue" → `react_vs_vue_20260311`
  - "AI safety trends 2025" → `ai_safety_trends_20260311`
- Create the directory if it doesn't exist

---

## File-by-File Generation

Generate each file individually. Write each file to disk immediately before moving to the next.

### 1. `summary.md` — Executive Summary

```markdown
# Research Summary: [Topic]

**Mode:** [Quick/Standard/Deep/UltraDeep]
**Sources:** [N] total
**Date:** [YYYY-MM-DD]
**Research Question:** [Original question]

## Key Findings

- **Finding 1:** [One-sentence summary with key data point] [1]
- **Finding 2:** [One-sentence summary with key data point] [5]
- **Finding 3:** [One-sentence summary with key data point] [9]
[Continue for all major findings]

## Primary Recommendation

[One clear, actionable sentence]

## Confidence Level

[High/Medium/Low] — [Brief justification]

## Scope & Methodology

[2-3 paragraphs: what was investigated, methods used, source count, time period]

## Key Assumptions

- [Assumption 1 and why it matters]
- [Assumption 2 and why it matters]
```

**Target:** 200-400 words. This is the entry point — keep it concise.

---

### 2. `findings/01_{title}.md` through `findings/NN_{title}.md`

One file per major finding. Number sequentially.

```markdown
# Finding: [Descriptive Title]

## Summary

[1-2 sentence summary of what was found]

## Evidence

[2-4 paragraphs presenting detailed evidence with specific data, statistics, dates.
Every factual claim followed by [N] citation in same sentence.
Use "According to [1]..." or "[1] reports..." patterns.]

## Key Data Points

- [Specific metric or statistic] [N]
- [Specific metric or statistic] [N]
- [Conflicting data if any] [N]

## Implications

[1-2 paragraphs on what this finding means for the user's question]

## Sources

[1], [3], [7], [12]
```

**Target:** 300-800 words per finding. Let evidence determine length — don't pad, don't truncate.

**Per-finding quality check:**
- [ ] ≥2 paragraphs of evidence
- [ ] ≥80% prose (not bullets)
- [ ] Every claim cited in same sentence
- [ ] Specific numbers, not vague statements

---

### 3. `synthesis.md` — Patterns & Insights

```markdown
# Synthesis & Insights

## Patterns Identified

[2-3 paragraphs identifying key patterns across findings.
Reference specific findings by number.]

## Novel Insights

[2-3 paragraphs of insights that go BEYOND what sources explicitly stated.
What emerges from connecting information across sources?]

## Implications

**For the research question:**
[Specific implications for the user's situation/decision]

**Broader implications:**
[Wider significance]

**Second-order effects:**
[What might happen as consequences]
```

**Target:** 500-1000 words.

---

### 4. `limitations.md` — Gaps & Caveats

```markdown
# Limitations & Caveats

## Counterevidence

[2-3 paragraphs explaining contradictory evidence found]

**Contradictory Finding 1:**
- Source: [Citation]
- Why it contradicts: [Explanation]
- Impact on conclusions: [Minimal/Moderate/Significant]

## Known Gaps

[2-3 paragraphs: what information was unavailable, what remains unanswered]

## Areas of Uncertainty

[Where sources disagree, where evidence is thin, what could change conclusions]
```

**Target:** 300-600 words.

---

### 5. `recommendations.md` — Actions & Next Steps

```markdown
# Recommendations

## Immediate Actions

1. **[Action Title]**
   - What: [Specific action]
   - Why: [Rationale from findings]
   - How: [Implementation steps]

2. **[Continue...]**

## Next Steps (1-3 months)

1. **[Step Title]** — [Details]

## Further Research Needed

1. **[Topic]** — [What to investigate and why it matters]
```

**Target:** 300-500 words.

---

### 6. `bibliography.md` — Complete Source List

```markdown
# Bibliography

[1] Author/Organization (Year). "Title". Publication. URL (Retrieved: YYYY-MM-DD)
[2] Author/Organization (Year). "Title". Publication. URL (Retrieved: YYYY-MM-DD)
[Continue for ALL citations used across all files]
```

**CRITICAL RULES:**
- Include EVERY citation [N] used across all output files
- NO placeholders: Never use "[8-75] Additional citations" or "etc."
- NO ranges: Write [3], [4], [5] individually, NOT "[3-50]"
- NO truncation: If 30 sources cited, write all 30 entries in full
- Each entry gets: Author/Org, Year, Title, Publication, URL, Retrieved date

---

## Citation Tracking

Maintain a running list of citations used across all files:

```
citations_used = [1, 2, 3, ...]
```

- After writing each file, add its new citations to the list
- In `bibliography.md`, generate an entry for EVERY number in `citations_used`
- Citation numbers must be consistent across all files

---

## Writing Standards (Apply to EVERY File)

Before considering any file complete, verify:

- [ ] **Prose-first**: ≥80% flowing prose, <20% bullets
- [ ] **No placeholders**: Zero "TBD", "TODO", "Content continues..."
- [ ] **Evidence-rich**: Specific data points, statistics, quotes
- [ ] **Citation density**: Major claims cited in same sentence
- [ ] **No vague attributions**: Never "research suggests..." or "experts believe..."

**Anti-Truncation:** Each file is small enough that truncation should never happen. If a finding needs >800 words, split it into sub-findings.
