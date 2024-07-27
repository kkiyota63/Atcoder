import bisect
import heapq

N, Q = map(int, input().split())
a = list(map(int, input().split()))
bk = [list(map(int, input().split())) for _ in range(Q)]
b, k = [list(i) for i in zip(*bk)]

# a をソートしておく
a.sort()

for i in range(Q):
    b_i = b[i]
    distances = []
    
    # 各 b[i] に対して全ての a との距離を計算
    for a_j in a:
        heapq.heappush(distances, abs(b_i - a_j))
    
    # k 番目の距離を取得
    for _ in range(k[i] - 1):
        heapq.heappop(distances)
    
    # k 番目の最小距離を出力
    print(heapq.heappop(distances))
