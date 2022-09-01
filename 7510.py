import sys
import math
n = int(sys.stdin.readline())

for i in range(1, n + 1):
    print(f"Scenario #{i}:")
    tri = list(map(int, sys.stdin.readline().split()))
    tri.sort(reverse=True)
    if math.pow(tri[0], 2) == math.pow(tri[1], 2) + math.pow(tri[2], 2):
        print("yes")
    else:
        print("no")
    print()
