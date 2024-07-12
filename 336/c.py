from itertools import product

def find_nth_even_digit_number(N):
    # 使用する数字
    digits = ['0', '2', '4', '6', '8']
    
    # 数値を格納するリスト
    number_list = []
    
    # 各桁数についてループ
    for length in range(1, 17):  # 必要な桁数に応じてループを設定
        combinations = product(digits, repeat=length)
        for comb in combinations:
            number = ''.join(comb)
            if number[0] != '0':  # 先頭の桁がゼロでない場合のみ追加
                number_list.append(number)
                if len(number_list) == N:  # N番目の数値を見つけたら終了
                    return number_list[N-1]

# Nを入力
N = int(input())
# N番目の数値を取得して表示
print(find_nth_even_digit_number(N-1))
