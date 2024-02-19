S = input()

if  S[0].isupper()== True: 
    for str in S[1:]:
        if str.isupper() == True:
            print("No")
            exit()
    print("Yes")
else:
    print("No")

