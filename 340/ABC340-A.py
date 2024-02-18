A,B,D = map(int, input().split())
NUM=[A]

#初項が A、末項が B、公差が D であるような等差数列
while A < B:
    A += D
    if A > B:
        break
    NUM.append(A)

#NUMを横書きで出力
for i in range(len(NUM)):
    print(NUM[i], end=" ")
print()
