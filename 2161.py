import sys

n = int(sys.stdin.readline())
stack = [i for i in range(1, n+1)]

while len(stack) != 1:
    print(stack.pop(0), end=' ')

    if len(stack) == 1:
        break
    else:
        card = stack.pop(0)
        stack.append(card)

print(stack[0])
