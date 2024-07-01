# from itertools import permutations

# W, B  =map(int, input().split())   
# S = "wbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbw"
# P = []

# P = ['w']*W + ['b']*B  

# all_patterns = set(permutations(P))

# found = False
# for i in all_patterns:
#     if ''.join(i) in S:
#         found = True
#         break

# if found:
#     print("Yes")
# else:
#     print("No")
    

# wとbの数を入力として取得
W, B = map(int, input().split())

# チェックする基本部分文字列
base_S = "wbwbwwbwbwbwwbw"

# 必要な長さの繰り返し文字列を作成
sub_len = W + B

# 基本部分文字列を十分な長さまで繰り返し
repeated_S = base_S * ((2 * sub_len // len(base_S)) + 1)

print(repeated_S)

# Sの中でwとbのカウントが一致する部分文字列があるかをチェック
found = False

for i in range(len(repeated_S) - sub_len + 1):
    sub_str = repeated_S[i:i + sub_len]
    if sub_str.count('w') == W and sub_str.count('b') == B:
        found = True
        break

# 結果を出力
if found:
    print('Yes')
else:
    print('No')




