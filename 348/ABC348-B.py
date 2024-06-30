N = int(input())
points = []
for i in range(N):
    X, Y = map(int, input().split())
    points.append([X, Y])

for i in range(N):
    max_distance = 0
    max_index = 0
    for j in range(N):
        distance = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5
        if distance > max_distance:
            max_distance = distance
            max_index = j
    print(max_index+1)