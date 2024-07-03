import sys
array = []
for i in sys.stdin.readlines():
    array.append(int(i.rstrip()))
print(array)
