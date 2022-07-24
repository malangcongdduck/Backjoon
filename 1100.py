import sys

count = 0
board = []
for _ in range(8):
    row = list(sys.stdin.readline())
    board.append(row)

for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0 and board[i][j] == 'F':
            count += 1
        elif i % 2 == 1 and j % 2 == 1 and board[i][j] == 'F':
            count += 1

print(count)
