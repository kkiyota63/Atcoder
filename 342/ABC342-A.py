from collections import Counter

S = input()

# 文字列の各文字の出現頻度を計算
char_freq = Counter(S)

# 出現頻度の最小値の文字を取得
min_freq = min(char_freq, key=char_freq.get)

cnt = 0

for i in range(len(S)):
    cnt += 1
    if S[i] == min_freq:
        print(cnt)
        break
    else:
        continue

