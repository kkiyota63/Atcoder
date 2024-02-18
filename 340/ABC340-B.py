A = []
B = []
q_num  = int(input())

for i in range(q_num):
    q,num=map(int, input().split())
    if q == 1:
        A.append(num)
    if q == 2:
        B.append(A[len(A)-num])

for i in  range(len(B)):
    print(B[i])



