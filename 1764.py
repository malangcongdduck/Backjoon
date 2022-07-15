import sys

n, m = map(int, sys.stdin.readline().split())

p = []
result = []

for i in range(n+m):
    s = str.strip((sys.stdin.readline()))
    p.append(s)

p.sort()

for i in range(n+m-1):
    j = i+1
    if p[i] == p[j]:
        result.append(p[i])

result.sort()

print(len(result))
for i in result:
    print(i)
