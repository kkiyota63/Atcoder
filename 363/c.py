from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def contains_k_length_palindromic_substring(s, K):
    n = len(s)
    for i in range(n - K + 1):
        if is_palindrome(s[i:i + K]):
            return True
    return False

def count_non_k_length_palindromic_permutations(S, K):
    # 文字列の順列を生成し、重複を避けるためにセットに格納
    perms = set(''.join(p) for p in permutations(S))
    
    non_palindromic_count = 0
    
    for perm_str in perms:
        if not contains_k_length_palindromic_substring(perm_str, K):
            non_palindromic_count += 1
    
    return non_palindromic_count

# 標準入力から文字列とKを受け取る
N ,K = map(int, input().split())   #NはKの長さ
S = input().strip()

# 長さKの回文を含まない順列の数を数えて表示
non_palindromic_count = count_non_k_length_palindromic_permutations(S, K)
print(non_palindromic_count)

