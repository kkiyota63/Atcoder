N = int(input())
a = list(map(int, input().split()))

alice = 0
bob = 0

for i in range(N):
    if i%2 == 0:
        alice+=max(a)
        a.remove(max(a))
    else:
        bob+=max(a)
        a.remove(max(a))

print(alice-bob)
    