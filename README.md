# 日本語ビジネス文書校正 Skill

**バージョン：1.2.1**

AIが作成した営業資料、提案書、会社案内、技術比較レポートなどを、日本企業の顧客向け資料として自然な日本語に整えるSkillです。

## 特徴
- 受動的な報告調を減らし、結果を直接伝える
- 英語の直訳調や過剰な敬語を修正
- 技術用語・数値・測定条件を維持
- 根拠のない断定や誇張表現を検出
- 校正結果と要確認事項を分けて提示

## 使い方

### Claude Code（プラグイン）
個人で入れる場合：

```
/plugin install japanese-business-quality --marketplace tigereye-ai/japanese-business-quality-skill
```

チーム全員に配布する場合は、組織管理者が管理画面の「プラグインと Skills」→「追加」→「GitHub から同期」でこのリポジトリを登録し、オーディエンスを「全員・デフォルトでインストール済み」に設定します。main ブランチへの変更は同期で反映されます。

プラグインには、日本語を含む `.md` / `.txt` ファイルの書き込み後に一次チェックを自動実行するフックが含まれます。

### その他のエージェント
Skill対応エージェントの所定ディレクトリ（例：`.agents/skills/japanese-business-quality/`）に `skills/japanese-business-quality/` の中身を配置し、`SKILL.md` を参照するよう設定します。登録方法は製品によって異なります。

指示例：

> japanese-business-qualityを使って、この提案書を校正してください。受動的な報告調を避け、結果を先に伝える自然な日本語にしてください。数値・モデル名・測定条件・技術仕様は変更せず、修正文と要確認事項を出してください。

## ファイル構成
- `skills/japanese-business-quality/SKILL.md`：日本語による校正指示
- `skills/japanese-business-quality/references/style-guide.md`：表現・文体・用語のルール
- `skills/japanese-business-quality/references/rubric.md`：採点基準
- `skills/japanese-business-quality/examples/before-after.md`：校正例
- `skills/japanese-business-quality/scripts/check_text.py`：UTF-8テキストの簡易検査
- `.claude-plugin/`：Claude Code のプラグイン・マーケットプレイス定義
- `hooks/`：書き込み後に一次チェックを実行するフック

## 一次チェック
```bash
python skills/japanese-business-quality/scripts/check_text.py input.txt --json
```
一次チェックは表現の候補を抽出するだけです。文脈の判断、書き換え、意味の照合にはLLMと人による確認が必要です。

## 更新履歴
- v1.2.1：Windows でフックが起動しない問題と、一次チェックの出力が文字化けする問題を修正
- v1.2：校正指示・表現基準・品質評価・例文を日本語主体に全面改訂
- v1.1：能動表現と結果先行の方針を追加
