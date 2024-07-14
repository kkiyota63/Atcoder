R , G ,B = map(int, input().split())
C = input()

if C == "Red":
    if G <  B:
        print(G)
    else:
        print(B)

elif C == "Green":
    if R < B:
        print(R)
    else:
        print(B)

elif C == "Blue":
    if R < G:
        print(R)
    else:
        print(G)