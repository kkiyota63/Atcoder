# 文字のペアごとの長さを定義
lengths = {
    'AC': 2,
    'AD': 2,
    'BD': 2,
    'BE': 2,
    'CE': 2,
    'AB': 1,
    'BC': 1,
    'CD': 1,
    'DE': 1,
    'EA': 1
}

# 入力を取得
S = input()
T = input()

def calculate_length(s):
    total_length = 0
    for i in range(len(s) - 1):
        pair = s[i] + s[i + 1]
        if pair in lengths:
            total_length += lengths[pair]
        else:
            # 逆順のペアも考慮する場合
            reverse_pair = pair[::-1]
            if reverse_pair in lengths:
                total_length += lengths[reverse_pair]
            else:
                return -1  # 定義されていないペアがあった場合
    return total_length

# それぞれの文字列の総距離を計算
length_S = calculate_length(S)
length_T = calculate_length(T)

# 比較して結果を出力
if length_S == length_T:
    print("Yes")
else:
    print("No")
