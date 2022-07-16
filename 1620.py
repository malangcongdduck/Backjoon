import sys

n, m = map(int, sys.stdin.readline().split())
book = []
result = []

for i in range(n):
    s = str.strip((sys.stdin.readline()))
    book.append(s)

for i in range(m):
    order = sys.stdin.readline()

    try:
        order = int(order)
        result.append(book[order-1])
    except:
        order = str.strip(order)
        result.append(book.index(order)+1)

for i in result:
    print(i)
