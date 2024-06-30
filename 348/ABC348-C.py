N = int(input())
groups = {}

# Cが同じものをグループ化する
for i in range(1, N+1):
    A, C = map(int, input().split())
    if C not in groups:
        groups[C] = []
    groups[C].append(A)

MinMax = 0

# 各グループのAの最小値の最大値を出力する
for C, As in groups.items():
    if(MinMax < min(As)):
        MinMax = min(As)

print(MinMax)