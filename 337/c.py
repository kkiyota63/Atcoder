N = int(input())
A = list(map(int, input().split()))
# B = []
# A_list = []

# # 1からNまでの数値リストを作成
# for i in range(N):
#     B.append(i + 1)
# B.sort()

# # AとBを結合
# for a, b in zip(A, B):
#     A_list.append((a, b))


# ans_list = []

# # -1 を持つ要素を探して ans_list に追加
# for k in range(len(A_list)):
#     if A_list[k][0] == -1:
#         ans_list.append(A_list[k][1])

# # ans_list の前の要素と一致する場合に追加
# for j in range(len(A_list)):
#     for k in range(len(A_list)):
#         if A_list[k][0] == ans_list[-1]:
#             ans_list.append(A_list[k][1])

# i = 0
# for i in  range(len(ans_list)):
#     print(ans_list[i], end=" ")
# print()


# 辞書を作成して、Aの要素と対応するインデックスを保持
A_dict = {i + 1: A[i] for i in range(N)}

# A_dictをキーでソート
sorted_A_dict = dict(sorted(A_dict.items()))

print("Sorted A_dict:", sorted_A_dict)

ans_list = []

# '-1' を持つ要素を探して ans_list に追加
for key, value in sorted_A_dict.items():
    if value == '-1':
        ans_list.append(key)
        print(f"append ({key}, {value})")

# ans_list の前の要素と一致する場合に追加
for key, value in sorted_A_dict.items():
    if len(ans_list) > 0 and value == str(ans_list[-1]):
        ans_list.append(key)
        print(f"append ({key}, {value})")

print("ans_list:", ans_list)