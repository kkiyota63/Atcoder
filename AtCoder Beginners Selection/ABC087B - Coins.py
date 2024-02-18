A = int(input())
B = int(input())
C = int(input())
X = int(input())

def calc(A, B, C, X):
    cnt = 0
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                if 500*a + 100*b + 50*c == X:
                    cnt += 1
    return cnt

print(calc(A, B, C, X))

#range(3)は0,1,2を返す