import sys

n = int(sys.stdin.readline())

for i in range(n):
    dot = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
    point = []
    for i in range(3):
        for j in range(i + 1, 4):
            point.append((dot[i][0]-dot[j][0])*(dot[i][0]-dot[j]
                                                [0])+(dot[i][1]-dot[j][1])*(dot[i][1]-dot[j][1]))
    point.sort()
    if point[0] == point[1] and point[0] == point[2] and point[0] == point[3] and point[4] == point[5]:
        print(1)
    else:
        print(0)
