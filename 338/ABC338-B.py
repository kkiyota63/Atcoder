from collections import Counter

S = input()
i = 0

# 文字列の各文字の出現頻度を計算
char_freq = Counter(S)

# 出現頻度の最大値を取得
max_freq = max(char_freq.values())

# 出現頻度が最大の文字を取得
max_S = [char for char, freq in char_freq.items() if freq == max_freq]
s = max_S[0]

for i in range(len(max_S)-1):
    if max_S[i+1] < s:
      s = max_S[i+1]

print(s)