N, A = map(int, input().split())
T = list(map(int, input().split()))
t = 0

for i in range(N):
    if t <= T[i]: #またないでいい時は、
        t = T[i] + A #出発時間に発行時間を足したものが、次の人の発行時間となる。
        print(t)
        continue
    #またないといけない時は、前の人が発行を終えた時間t[i-1]に発行時間Aを足す。
    t += A
    print(t)






