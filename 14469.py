import sys

n = int(sys.stdin.readline())
cows = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    cows.append([a, b])

cows.sort(key=lambda x: x[0])

time = cows[0][0] + cows[0][1]
for i in range(1, n):
    if time < cows[i][0]:
        time = cows[i][0]

    time += cows[i][1]

print(time)
