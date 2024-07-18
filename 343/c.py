N = list(map(int, input().split()))

# 前からi番目と最後からi番目を比較
for i in range(1, len(N) + 1):
    if N[i-1] != N[-i]:
        print('No')
        break
else:
    print('Yes')
