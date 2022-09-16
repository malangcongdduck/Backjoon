import sys
from itertools import permutations

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
pli = permutations(li, n)

result = 0

for p in pli:
    diff = 0
    for i in range(len(p)-1):
        diff += abs(p[i] - p[i+1])

    if diff > result:
        result = diff

print(result)
