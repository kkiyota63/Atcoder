# 入力の受け取り
S, T = map(str, input().split())
w = len(S)
result = []

# 文字列を指定した文字数ごとに分割する関数
def split_string(s, chunk_size):
    result = []
    for i in range(0, len(s), chunk_size):
        result.append(s[i:i + chunk_size])
    return result

if len(T)==1:
    print("No")
    exit()

# 各iごとにSの文字列を区切る
for i in range(1, w):  # 1から始めることでゼロ除算を回避
    result = split_string(S, i)
    #print(f"size {i}: {result}")
    
    if len(result) > 1:
        combined_result = ''
        for j in range(i):  # 分割サイズに基づいて各位置の文字を集める
            for segment in result:
                if j < len(segment):
                    combined_result += segment[j]
        #print(combined_result)
        if (T in combined_result):
            print('Yes')
            exit()
print('No')
