N = int(input())

# パターンの最初の1を追加
pattern_str = "1"

for i in range(N):
    # 各繰り返しで0と1を追加
    pattern_str += "0"
    pattern_str += "1"

# 最終的なパターンを出力
print(pattern_str)