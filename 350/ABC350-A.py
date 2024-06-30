# 文字列を入力
S = input()

# 最初の3文字を文字列に変換
first_three = S[:3]

# 最後の文字を数値に変換
last_char = int(S[-3:])

#print("最初の3文字:", first_three)
#print("最後の文字(数値):", last_char)

if(len(S)==6):
    if(first_three == "ABC"):
        if(last_char <= 349 and last_char >= 1 and last_char != 316):
            print("Yes")
        else:
            print("No")
    else:
            print("No")
else:
    print("No")