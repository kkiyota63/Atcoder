N = int(input())
ans = 0

binary_str = bin(N)[2:]

binary_list = list(binary_str)

# リストを逆順にする
binary_list.reverse()

#print(binary_list)


for i in range(N):
    if binary_list[i] == '0':
        ans += 1
    else:
        break

print(ans)