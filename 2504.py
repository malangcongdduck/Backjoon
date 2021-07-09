import sys
from collections import deque

q = deque()
sen = sys.stdin.readline().strip()

result = 0
temp = 0
for i in sen:

    if i == ')':
        temp = 0
        while q:
            item = q.pop()

            if item == '(':
                if temp != 0:
                    q.append(temp * 2)
                else:
                    q.append(2)
                break

            elif item == '[':
                print(0)
                exit(0)

            else:
                temp += item

    elif i == ']':
        temp = 0
        while q:
            item = q.pop()

            if item == '[':
                if temp != 0:
                    q.append(temp * 3)
                else:
                    q.append(3)
                break

            elif item == '(':
                print(0)
                exit(0)

            else:
                temp += item

    else:
        q.append(i)


for i in q:
    if i == '(' or i == '[':
        print(0)
        exit(0)
    else:
        result += i

print(result)
