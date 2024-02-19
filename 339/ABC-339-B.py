import numpy as np

H, W, N = map(int, input().split())
flg = 0 # 0:上, 1:右, 2:下, 3:左

# H x W のグリッドを'.'で初期化
M = np.full((H, W), '.')

#kとlを初期化することで初期位置を設定
k = 0
l = 0

while N > 0:
    if M[k][l] == '.':
        M[k][l] = '#'  # 現在のマスを塗る
        #時計回りに移動する
        if flg == 0:
            l += 1
            if l > W:
                l= 0
            flg = 1
        elif flg == 1:
            k += 1
            if k > H:
                k = 0
            flg = 2
        elif flg == 2:
            l -= 1
            if l <0:
                l = W
            flg = 3
        elif flg == 3:
            k -= 1
            if k < 0:
                k = H
            flg = 0
    else:
        M[k][l] = '.'
        #反時計回りに移動する
        if flg == 0:
            k += 1
            if k > H:
                k = 0
            flg = 3
        elif flg == 3:
            l += 1
            if l > W:
                l = 0
            flg = 2
        elif flg == 2:
            k -= 1
            if k < 0:
                k = H
            flg = 1
        elif flg == 1:
            l -= 1
            if l <0:
                l = W
            flg = 0
    
    N-=1
    # グリッドの表示（オプション）
    print(N)
    print(k,l)
    for i in range(H):  # 各行に対して
        for j in range(W):  # 各列に対して
            print(M[i, j], end="")  # 同じ行の要素は改行せずに出力
        print()  # 各行の最後に改行を出力
    print()  # グリッドの最後に改行を出力

    


