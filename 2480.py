import sys
from collections import Counter

num = list(map(int, sys.stdin.readline().split()))

num_list = Counter(num)
sorted_num_list_value = sorted(
    num_list.items(), key=lambda item: item[1], reverse=True)

if sorted_num_list_value[0][1] == 3:
    print(10000 + int(sorted_num_list_value[0][0]) * 1000)
elif sorted_num_list_value[0][1] == 2:
    print(1000 + int(sorted_num_list_value[0][0]) * 100)
else:
    sorted_num_list_key = sorted(
        num_list.items(), key=lambda item: item[0], reverse=True)
    print(int(sorted_num_list_key[0][0]) * 100)
