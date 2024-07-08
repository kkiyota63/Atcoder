#動的計画法の実装の練習
#こちらの記事を参考にした
#https://qiita.com/keisuke-ota/items/504d66092671a67c1040

#実装の流れ、
#1.DP配列を用意する。
#2.初期条件を設定する。
#3.DP配列の漸化式を考える。
#4.DP配列の末尾を出力する。

N = int(input())
h = list(map(int, input().split()))

#DP配列を用意
dp = [0] * N

#初期条件を設定
#足場1から足場iへの最小コストをdp[i]とする
dp[0] = 0
dp[1] = abs(h[1] - h[0])

#DP配列の漸化式を考える
for i in range(2,N):
    #iを現在の足場とする
    #i-1とi-2からiに移動する場合の最小コストを考える
    dp[i] = min(h[i-2]+abs(h[i]-h[i-2]),h[i-1]+abs(h[i]-h[i-1]))

#DP配列の末尾を出力する
print(dp[N-1])
