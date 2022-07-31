import sys

n = int(sys.stdin.readline())

book = dict()
for _ in range(n):
    name = sys.stdin.readline().rstrip()

    if name in book:
        book[name] += 1
    else:
        book[name] = 1

max_book = [name for name, num in book.items() if max(book.values()) == num]
max_book.sort()
print(max_book[0])
