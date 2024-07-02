import math

X = int(input())

# X が二桁以上かを確認
if X >= 10:
    # 文字列に変換して処理
    X_str = str(X)
    #最後の文字列が0であることを確認
    if X_str[-1] == '0':
        new_number = X_str[:-1]
        print(new_number)
        exit()
    # 最後の数字を消去
    new_number_str = X_str[:-1]
    # 最後から二番目の数字に1を足す
    new_number = int(new_number_str) + 1
    print(new_number)
elif X <= -10 :
    X_str = str(X)
    if X_str[-1] == '0':
        new_number = X_str[:-1]
        print(new_number)
        exit()
    # new_number_str = X_str[:-1]
    # new_number = int(new_number_str) - 1
    # print(new_number)
else:
    print(math.ceil(X / 10))