def is_palindrome(s):
    return s == s[::-1]

def can_add_char(current, char, K):
    # 現在の文字列に char を追加しても、長さ K の回文部分文字列ができないか確認
    new_str = current + char
    if len(new_str) < K:
        return True
    return not is_palindrome(new_str[-K:])

def count_non_k_length_palindromic_permutations(S, K):
    from collections import Counter

    def backtrack(path, counter):
        if len(path) == len(S):
            return 1
        count = 0
        for char in counter:
            if counter[char] > 0 and can_add_char(path, char, K):
                counter[char] -= 1
                count += backtrack(path + char, counter)
                counter[char] += 1
        return count

    counter = Counter(S)
    return backtrack("", counter)

# 標準入力から文字列とKを受け取る
N, K = map(int, input().split())  # N は S の長さ
S = input().strip()

# 長さ K の回文を含まない順列の数を数えて表示
non_palindromic_count = count_non_k_length_palindromic_permutations(S, K)
print(non_palindromic_count)
