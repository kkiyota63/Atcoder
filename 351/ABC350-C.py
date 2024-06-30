N = int(input())
A = list(map(int, input().split()))

#ボールの数をカウント
cnt = 0
#からのリストを作成
sorted_list = []


for i in range(N):
    #リストにAを格納
    sorted_list.append(A[i])
    cnt += 1
    #1. もしリストの中が一個ならスキップ
    if len(sorted_list) == 1:
        continue
    #2. もしリストの中の一つ前の要素と異なるならスキップ
    if sorted_list[i] != sorted_list[i-1]:
        continue
    #3. もしリストの中の一つ前の要素と同じなら足す
    if sorted_list[i] == sorted_list[i-1]:
        A[i-1] += A[i]
        cnt -= 1 
        N -= 1
        continue
             

print(cnt)
