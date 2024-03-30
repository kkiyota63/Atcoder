N = int(input())

#N個のPをinput
P = list(map(int, input().split()))
Q = int(input())

#Q個のA,Bをinput
for i in range(Q):
    A, B = map(int, input().split())


    for j in range(N):
            if P[j] == A:
                print(A)
                break
            elif P[j] == B:
                print(B)
                break






