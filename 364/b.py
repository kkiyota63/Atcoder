H, W = map(int, input().split())
Si, Sj = map(int, input().split())
a = [list(input().strip()) for _ in range(H)]
X = input().strip()

# 0-based index
Si -= 1
Sj -= 1

# Directions: Up, Left, Down, Right
directions = {
    'U': (-1, 0),
    'L': (0, -1),
    'D': (1, 0),
    'R': (0, 1)
}

current_i, current_j = Si, Sj

for move in X:
    di, dj = directions[move]
    new_i, new_j = current_i + di, current_j + dj
    
    # Check if the new position is within bounds and not a blocked cell
    if 0 <= new_i < H and 0 <= new_j < W and a[new_i][new_j] == '.':
        current_i, current_j = new_i, new_j

# 1-based index
final_position = (current_i + 1, current_j + 1)
print(final_position[0], final_position[1])
