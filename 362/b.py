# 入力を受け取る
points = [list(map(int, input().split())) for _ in range(3)]

# 各点を変数に格納
x1, y1 = points[0]
x2, y2 = points[1]
x3, y3 = points[2]

# 辺の長さの平方を計算
AB2 = (x2 - x1) ** 2 + (y2 - y1) ** 2
BC2 = (x3 - x2) ** 2 + (y3 - y2) ** 2
CA2 = (x1 - x3) ** 2 + (y1 - y3) ** 2

# 直角三角形の判定
is_right_triangle = (AB2 + BC2 == CA2) or (BC2 + CA2 == AB2) or (CA2 + AB2 == BC2)

# 結果を出力
if is_right_triangle:
    print("Yes")
else:
    print("No")
