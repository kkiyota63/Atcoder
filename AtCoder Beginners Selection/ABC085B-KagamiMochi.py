N = int(input())
d = [0]*N

for i in range(N):
    d[i] = int(input())

#段数をカウントする変数
cnt = 0
stack_list = []

for i in range(N):
    if d == []:
        break
    if len(stack_list) == 0:
        stack_list.append(max(d))
        d = [x for x in d if x != max(d)]
        cnt += 1
        continue
    if min(stack_list)> max(d):
        stack_list.append(max(d))
        #dからmax(d)をすべて削除
        d = [x for x in d if x != max(d)]
        cnt += 1

print(cnt)