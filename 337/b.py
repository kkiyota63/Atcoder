S = input()

for i in range(len(S)-1):
    if(len(S)==1):
         break
    if (S[i]=="B" and S[i+1]=="A"):
        print("No")
        exit()
    elif (S[i]=="C" and S[i+1]=="A"):
        print("No")
        exit()
    elif (S[i]=="C" and S[i+1]=="B"):
        print("No")
        exit()

print("Yes") 