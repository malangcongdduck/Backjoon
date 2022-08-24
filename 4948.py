import sys

while True:
    min = int(sys.stdin.readline())
    if min == 0:
        break
    elif min == 1:
        print(1)
        continue

    max = 2 * min
    count = 0
    for i in range(min + 1, max + 1):
        flag = 1
        for j in range(2, int(pow(i, 0.5)) + 1):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            count += 1

    print(count)
