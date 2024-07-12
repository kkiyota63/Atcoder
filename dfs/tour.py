N, M = map(int, input().split())
A, B = map(list, input().split())
road = []

road[A].append(B)

def dfs(pos):
    print(pos, end=' ')         
    for i in A[pos]:
        dfs(i)

dfs(0)

#[1,2][2,3][3,2]  [1->2][2->3][3->2]
#[1,2,3]
#[2,3,2]で与えられているから、A[0]がB[[A0]]を参照し、それがA[B[A[0]]]を参照する。同じになったら終わり。
