import sys

a, b = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
bookmark = [abs(int(sys.stdin.readline()) - b) for _ in range(n)]

print(min(abs(a-b), min(bookmark)+1))
