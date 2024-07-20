def is_palindrome(num):
    return str(num) == str(num)[::-1]

def nth_palindrome(N):
    count = 0
    num = 0
    while True:
        if is_palindrome(num):
            count += 1
            if count == N:
                return num
        num += 1

N = int(input())
result = nth_palindrome(N)
print(result)
