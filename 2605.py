import sys

n = int(sys.stdin.readline())
order = list(map(int, sys.stdin.readline().split()))
people = []

for i in range(n):
    people.insert(i-order[i], i+1)

for i in people:
    print(i, end=' ')
