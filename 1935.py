import sys
n = int(sys.stdin.readline())
math = list(str.strip(sys.stdin.readline()))
stack = []
numbers = [0] * n

for i in range(n):
    numbers[i] = int(sys.stdin.readline())


for i in math:

    if 'A' <= i <= 'Z':
        stack.append(numbers[ord(i)-65])

    else:
        if len(stack) >= 2:
            num_1 = stack.pop()
            num_2 = stack.pop()

            if i == '+':
                cal = num_2 + num_1
            elif i == '*':
                cal = num_2 * num_1
            elif i == '/':
                cal = num_2 / num_1
            elif i == '-':
                cal = num_2 - num_1

            stack.append(cal)

        else:
            exit(0)

print("{:.2f}".format(stack[0]))
