def find_integer_sequence(N, intervals):
    L = [interval[0] for interval in intervals]
    R = [interval[1] for interval in intervals]
    
    sum_L = sum(L)
    sum_R = sum(R)
    
    # If sum of minimum values is greater than 0 or sum of maximum values is less than 0
    if sum_L > 0 or sum_R < 0:
        return "No"
    
    # Initialize X with minimum values
    X = L[:]
    current_sum = sum_L
    
    # Adjust to make sum(X) = 0
    for i in range(N):
        if current_sum == 0:
            break
        max_increment = R[i] - L[i]
        increment = min(max_increment, -current_sum)
        X[i] += increment
        current_sum += increment
    
    if current_sum != 0:
        return "No"
    
    return X

# Input reading
N = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(N)]

result = find_integer_sequence(N, intervals)
if result == "No":
    print(result)
else:
    print("Yes")
    print(" ".join(map(str, result)))
