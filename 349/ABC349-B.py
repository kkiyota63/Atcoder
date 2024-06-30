# S = input()
# count_dict = {}

# for char in S:
#     if char in count_dict:
#         count_dict[char] += 1
#     else:
#         count_dict[char] = 1

# count_1 = 0
# count_2 = 0 
# count_3 = 0
# count_more_than_3 = 0

# for count in count_dict.values():
#     if count == 1:
#         count_1 += 1
#     elif count == 2:
#         count_2 += 1
#     elif count == 3:
#         count_3 += 1
#     elif count >= 4:
#         count_more_than_3 += 1

# if (len(S)>=1) and (len(S)<=100) and ((count_1 == 0) or (count_1 == 2)) and ((count_2 == 0) or (count_2 == 2)) and ((count_3 == 0) or (count_3 == 2)) and (count_more_than_3 == 0):
#     print("Yes")
# else:
#     print("No")


from collections import Counter

S = input()
c = Counter(S)
d = Counter(c.values())
print("Yes" if set(d.values())== set([2]) else "No")