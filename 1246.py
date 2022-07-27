import sys

n, m = map(int, sys.stdin.readline().split())
pi = [0] * m
max_profit = 0
price = 0

for i in range(m):
    pi[i] = int(sys.stdin.readline())

pi.sort(reverse=True)

for i in range(m):
    if i + 1 > n:
        profit = pi[i] * n
    else:
        profit = (i+1) * pi[i]

    if profit > max_profit:
        max_profit = profit
        price = pi[i]

print(price, max_profit)
