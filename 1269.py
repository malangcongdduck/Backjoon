import sys

num_a, num_b = map(int, sys.stdin.readline().split())
a = set(list(map(int, sys.stdin.readline().split())))
b = set(list(map(int, sys.stdin.readline().split())))

df_set1 = a-b
df_set2 = b-a

print(len(df_set1) + len(df_set2))
