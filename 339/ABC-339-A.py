# 正規表現
import re

S = input()

# '.'以降の文字列を検索する正規表現パターン
pattern = '.*\.(.*)$'

# 正規表現で検索
match = re.search(pattern, S)

result = match.group(1)  # '.'以降の文字列を取得

print(result)