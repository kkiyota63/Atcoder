def dfs(pos):
    print(pos, end=' ')
    for i in tree[pos]:
        dfs(i)

tree = [[1, 2, 3],  [4, 5], [], [6, 7], [8, 9], [], [10], [], [], [], []]
dfs(0)