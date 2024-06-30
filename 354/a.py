H = int(input())
M = 0
i = 0
while True:
    M += 2**i
    if(M>H):
        print(i+1)
        break
    i += 1