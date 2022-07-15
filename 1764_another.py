import sys

n, m = map(int, sys.stdin.readline().split())

p1 = set()
p2 = set()

for i in range(n):
    p1.add(str.strip((sys.stdin.readline())))

for i in range(m):
    p2.add(str.strip((sys.stdin.readline())))


result = sorted(list(p1 & p2))

print(len(result))
for i in result:
    print(i)
