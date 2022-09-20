import sys

n = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
sum = 0
min_p = price[0]

for i in range(n-1):
    if min_p > price[i]:
        min_p = price[i]
    sum += min_p * road[i]

print(sum)
