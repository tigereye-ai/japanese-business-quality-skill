---
name: japanese-business-quality
description: Review and revise Japanese customer-facing business documents for natural native Japanese, appropriate business register, terminology consistency, and evidence integrity. Use for proposals, sales decks, company profiles, customer emails, reports, and document text. Preserve facts, numbers, product names, legal commitments, and intended meaning.
---
# Japanese Business Quality

## Purpose
Edit Japanese business-facing text to sound like it was written by an experienced native Japanese enterprise sales, consulting, or corporate planning professional. Prioritize factual fidelity over fluency.

## Workflow
1. Identify audience, document purpose, industry, and expected formality. If unspecified, assume Japanese B2B customer-facing materials with clear, restrained です・ます style for prose and concise noun phrases for slide headings.
2. Extract text while preserving document hierarchy, table relationships, numbers, references, citations, and speaker notes where available.
3. Flag awkward translationese, excessive honorifics, vague marketing language, grammatical errors, inconsistent terminology, unclear subjects, unsupported assertions, and logical discontinuities.
4. Rewrite each passage with the minimum necessary changes. Preserve all claims, amounts, dates, specifications, product names, scope, and responsibility allocations. Never invent metrics, customers, certifications, guarantees, or citations.
5. Verify the revised text against the original for semantic equivalence and factual consistency. Mark ambiguous or unverifiable claims for human review instead of silently fixing them.
6. Return revised copy, a concise change log, issues requiring confirmation, and a quality score. When editing a file, preserve layout and formatting as far as possible and inspect for overflow.

## Hard constraints
- Never alter numbers, units, dates, pricing, contractual terms, legal disclaimers, brand names, model identifiers, or technical capabilities without explicit instruction.
- Do not upgrade aspirational statements into guarantees; distinguish planned, under development, demonstrated, and production-ready.
- Do not add unsupported superlatives such as 業界最高, 完全, 必ず, 100%, 圧倒的.
- Preserve the intended level of politeness; avoid redundant させていただく and excessive 弊社/貴社.
- Do not replace precise technical terms with imprecise generalizations.
- Treat quotations, citations, and regulatory language as protected; propose changes separately.
- If the source is unclear, label 要確認 and explain why.

## Quality rubric
Rate each dimension 1–5: grammatical correctness, native fluency, business appropriateness, clarity, terminology consistency, factual fidelity, evidence discipline. Calculate a 100-point score using weights in references/rubric.md. Factual fidelity is a hard gate: if a material meaning change is detected, do not mark the document approved regardless of total score.

## Output format
### 修正文
[final copy]
### 主な修正
[original -> revised, reason]
### 要確認事項
[only unresolved questions]
### 品質評価
[score and approval status]

## Supporting files
- `references/style-guide.md`: detailed Japanese editorial conventions.
- `references/rubric.md`: scoring and release criteria.
- `examples/before-after.md`: example rewrites.
- `scripts/check_text.py`: deterministic first-pass linting of UTF-8 text.

## Native Japanese voice: active, direct, result-first (mandatory)
- Prefer active constructions with a clear actor or a direct statement of the result. Avoid repetitive passive/reporting endings such as 「確認されました」「示されました」「評価されました」「期待されます」「実施されました」.
- Do not mechanically replace every passive with 「確認しました」. Prefer concrete findings: 「検出できることが確認されました」→「10件中9件を検出しました」.
- Avoid report-template padding such as 「〜という結果が得られました」「〜であることが明らかになりました」 when the finding itself can be stated directly.
- Prefer concise, native B2B prose, using subject omission only where unambiguous. For slides use result-oriented headings and compact declarative statements.
- Keep passive constructions when the affected party/state is the natural topic (e.g. 「個人情報は暗号化されます」), or when agency is genuinely unknown or material.
- Do not turn inference into observation, or promise into fact. Retain measured sample sizes, conditions and uncertainty.
- During QA, count repetitive passive/reporting endings and revise clusters; verify that every rewrite preserves the original actor, agency, certainty and technical meaning.
