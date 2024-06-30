N = int(input())
sum_x = 0
sum_y = 0

for i in range(N):
    X,Y = map(int, input().split())
    sum_x += X
    sum_y += Y

if(sum_x > sum_y):
    print("Takahashi")
elif(sum_x < sum_y):
    print("Aoki")
else:
    print("Draw")

