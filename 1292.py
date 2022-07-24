import sys

a, b = map(int, sys.stdin.readline().split())

nums = [0]
for i in range(46):
    for j in range(i):
        nums.append(i)

print(sum(nums[a:b+1]))
