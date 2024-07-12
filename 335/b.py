def find_combinations_up_to_N(N):
    combinations = []
    for n in range(N + 1):
        for x in range(n + 1):
            for y in range(n + 1 - x):
                z = n - x - y
                combinations.append((x, y, z))
    return combinations

N = int(input())
all_combinations = find_combinations_up_to_N(N)

# (x, y, z) の順にソート
sorted_combinations = sorted(all_combinations)

for combo in sorted_combinations:
    print(f"{combo[0]} {combo[1]} {combo[2]}")
