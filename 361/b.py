def is_overlapping(cube1, cube2):
    # cube1とcube2の各頂点を取得
    (a, b, c, d, e, f) = cube1
    (g, h, i, j, k, l) = cube2
    
    # cube1の最小頂点と最大頂点を計算
    min1 = (min(a, d), min(b, e), min(c, f))
    max1 = (max(a, d), max(b, e), max(c, f))
    
    # cube2の最小頂点と最大頂点を計算
    min2 = (min(g, j), min(h, k), min(i, l))
    max2 = (max(g, j), max(h, k), max(i, l))
    
    # 重なりの条件をチェック
    overlap_x = min1[0] < max2[0] and max1[0] > min2[0]
    overlap_y = min1[1] < max2[1] and max1[1] > min2[1]
    overlap_z = min1[2] < max2[2] and max1[2] > min2[2]
    
    return overlap_x and overlap_y and overlap_z

# ユーザー入力から直方体の頂点の座標を取得
a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

# 判定
cube1 = (a, b, c, d, e, f)
cube2 = (g, h, i, j, k, l)

if is_overlapping(cube1, cube2):
    print("Yes")
else:
    print("No")
