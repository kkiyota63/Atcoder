S = input()

# 先頭が '<' であることを確認
if S[0] != '<':
    print("No")
    exit()

# 最後が '>' であることを確認
if S[-1] != '>':
    print("No")
    exit()

# 中間の文字が全て '=' であることを確認
for i in range(1, len(S) - 1):
    if S[i] != '=':
        print("No")
        exit()

# すべての条件を満たしていれば "Yes" を出力
print("Yes")
