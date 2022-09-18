import sys


def distance(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])


n = int(sys.stdin.readline())
checkpoint = [list(map(int, sys.stdin.readline().split()))]
total = 0
final_skip = 0

for i in range(1, n):
    checkpoint.append(list(map(int, sys.stdin.readline().split())))
    total += distance(checkpoint[i-1], checkpoint[i])

for i in range(1, n-1):
    no_skip = distance(checkpoint[i-1], checkpoint[i]) + \
        distance(checkpoint[i], checkpoint[i+1])
    skip = distance(checkpoint[i-1], checkpoint[i+1])
    final_skip = max(final_skip, abs(no_skip-skip))

print(total-final_skip)
