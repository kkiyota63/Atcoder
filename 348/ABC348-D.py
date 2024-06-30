H, W = map(int, input().split())
grid = []
for i in range(H):
    row = list(input())
    grid.append(row)

N = int(input())
for k in range(N):  
    R, C, E = map(int, input().split())


# 起点を(0, 0)に設定
start_row, start_col = 0, 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            start_row, start_col = i, j
            energy = E
            break
    

# グリッドを移動
while energy > 0:
    if 0 <= start_row < H and 0 <= start_col < W and grid[start_row][start_col] == '.':
        if grid[i][j] == 'T':
            print("Yes")
            break
        # 移動可能な場合は、エネルギーを消費して移動する
        energy -= 1
        start_row, start_col = R, C
    else:
        # 移動不可能な場合は、ゴールに到達できない
        print("No")
        break