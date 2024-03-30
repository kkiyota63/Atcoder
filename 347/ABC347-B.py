S = input()

count = 0
seen = set()  # 既に登場した部分文字列を格納するセット

for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        substring = S[i:j]
        if substring not in seen:
            seen.add(substring)
            count += 1

print(count)