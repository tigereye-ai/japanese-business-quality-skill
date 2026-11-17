# Japanese Business Quality Skill

Copy this folder into your agent's skills directory (for example, `.agents/skills/japanese-business-quality/`) and have the agent read `SKILL.md` when reviewing Japanese customer-facing documents. Exact installation and invocation depend on the agent platform.

Example instruction: `この提案書を japanese-business-quality の Standard モードで校正してください。数値・製品名・技術仕様を維持し、修正文、変更履歴、要確認事項、品質評価を出してください。`

Quick deterministic lint: `python scripts/check_text.py input.txt --json`

The lint script only flags some patterns; substantive rewriting and semantic verification require a language model and human review for high-stakes claims.

### v1.1 更新
顧客向け資料で多用される「確認されました」「示されました」などの受動的・翻訳調の表現を抑え、結果先行の自然な能動表現を優先する規則を追加しました。
