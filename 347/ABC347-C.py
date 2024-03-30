# 入力を受け取る
N, A, B = map(int, input().split())
D = list(map(int, input().split()))

# 休日の範囲を計算する
start_holiday = 1
end_holiday = A

# 1週間の範囲を計算する
one_week = A + B

# 全ての予定が休日に含まれるかを判定
can_all_be_holidays = True
for day in D:
    # 予定の日付が休日の範囲内にあるかを探す
    found = False
    orig_day = day
    while not found:
        # 予定の日付が休日の範囲内にあれば探索終了
        if start_holiday <= day <= end_holiday:
            found = True
            break
        # 範囲外の場合は1週間ずらして再チェック
        day = (day - 1) % one_week + 1
        # 元の日付に戻ってきたら探索終了
        if day == orig_day:
            break

    # 休日の範囲内に該当する日付が見つからなかった場合
    if not found:
        can_all_be_holidays = False
        break

# 結果を出力
if can_all_be_holidays:
    print("Yes")
else:
    print("No")