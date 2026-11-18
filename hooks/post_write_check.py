#!/usr/bin/env python3
"""PostToolUse hook: 日本語のテキスト文書が書き込まれたら一次チェックを実行する。

指摘があれば stderr に出して exit 2 を返し、Claude に修正検討を促す。
対象外のファイルや指摘なしの場合は何もせず exit 0。
"""
import json
import pathlib
import re
import sys

TARGET_SUFFIXES = {'.md', '.markdown', '.txt'}
JAPANESE = re.compile(r'[぀-ヿ一-鿿]')

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent
                       / 'skills' / 'japanese-business-quality' / 'scripts'))
from check_text import lint  # noqa: E402


def main():
    # Claude Code は UTF-8 で読むため、Windows（cp932）でも文字化けしないよう UTF-8 に固定する
    sys.stderr.reconfigure(encoding='utf-8')
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    file_path = (payload.get('tool_input') or {}).get('file_path')
    if not file_path:
        return 0
    path = pathlib.Path(file_path)
    if path.suffix.lower() not in TARGET_SUFFIXES or not path.is_file():
        return 0
    try:
        text = path.read_text(encoding='utf-8')
    except (OSError, UnicodeDecodeError):
        return 0
    if not JAPANESE.search(text):
        return 0
    issues = lint(text)
    if not issues:
        return 0
    lines = [f'[japanese-business-quality] {path.name} の一次チェックで {len(issues)} 件の候補があります。'
             '顧客向け文書であれば japanese-business-quality スキルの基準で確認してください。']
    lines += [f"  {i['line']}行目: {i['match']} — {i['issue']}" for i in issues]
    print('\n'.join(lines), file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main())
