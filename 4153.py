import sys

while True:
    nums = list(map(int, sys.stdin.readline().split()))

    if nums[0] == 0 and nums[0] == 0 and nums[0] == 0:
        break
    else:
        nums.sort()
        if pow(nums[0], 2) + pow(nums[1], 2) == pow(nums[2], 2):
            print("right")
        else:
            print("wrong")
