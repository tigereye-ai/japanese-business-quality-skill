#!/usr/bin/env python3
"""First-pass Japanese business copy lint. No automatic factual rewrites."""
import argparse
import json
import pathlib
import re
import sys

RULES = [
    (r'シームレスな(?:体験|ソリューション)', '抽象的なカタカナ表現：具体的な業務内容を確認'),
    (r'エンパワー', '英語直訳調：具体的な支援内容を記載'),
    (r'最適化させていただ', '過剰な敬語・不自然な使役'),
    (r'圧倒的|業界(?:最高|No\.1)|完全自動化|100%', '根拠・適用範囲の確認が必要な強い主張'),
    (r'革新的なソリューション', '抽象表現：提供価値を具体化'),
]

def lint(text):
    issues = []
    for pattern, message in RULES:
        for match in re.finditer(pattern, text):
            issues.append({'line': text.count('\n', 0, match.start()) + 1,
                           'match': match.group(0), 'issue': message})
    return issues

if __name__ == '__main__':
    # 日本語版 Windows のコンソール（cp932）でも出力できるよう UTF-8 に固定する
    sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=pathlib.Path)
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    issues = lint(args.input.read_text(encoding='utf-8'))
    if args.json:
        print(json.dumps(issues, ensure_ascii=False, indent=2))
    else:
        for issue in issues:
            print(f"{issue['line']}: {issue['match']} — {issue['issue']}")
        print(f'{len(issues)} issue(s)')
