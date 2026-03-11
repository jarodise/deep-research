# Deep Research Evaluation Cases

Run these tests to evaluate the skill's performance and regression test across updates.

## Case 1: Quick Market Overview (Quick Mode)
**Prompt:** "Do a quick deep research on the AI agent framework landscape in early 2025. Compare LangChain, AutoGen, and CrewAI."
**Expected Mode:** Quick
**Success Criteria:**
- Completes in < 5 minutes
- Identifies at least 10 sources
- Accurately compares the 3 frameworks with recent (2024/2025) data
- Generates required modular files (`summary.md`, `findings/`, etc.)

## Case 2: Technical/Academic Deep Dive (Standard/Deep Mode)
**Prompt:** "Please research the state of the art in quantum error correction. Focus on surface codes and recent breakthroughs at major labs like Google and IBM."
**Expected Mode:** Standard or Deep
**Success Criteria:**
- Uses domain-specific searches (e.g., arxiv.org, academic papers)
- Triangulates complex technical claims with 3+ sources
- Explains limitations and current bottlenecks explicitly in `limitations.md`
- No hallucinated citations (verified by DOI/URL check)

## Case 3: Business Decision (UltraDeep Mode)
**Prompt:** "I need an ultradeep research report on migrating a large enterprise application from monolithic PostgreSQL to a distributed database like CockroachDB or built-in sharding. What are the hidden costs, failure modes, and real-world disaster stories?"
**Expected Mode:** UltraDeep
**Success Criteria:**
- Conducts 30+ source retrieval
- Goes beyond surface benefits and explicitly red-teams the decision in `synthesis.md` and `limitations.md`.
- Finds real-world post-mortems or failure stories
- Provides a clear, actionable recommendation in `recommendations.md`

## Evaluation Runner
To test the skill's output formatting without running a full research cycle:
```bash
python scripts/validate_report.py --report /path/to/generated/workspace/topic_dir/
```
