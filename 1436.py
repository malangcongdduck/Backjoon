import sys

n = int(sys.stdin.readline())
end = 666

while True:
    if '666' in str(end):
        n -= 1

    if n == 0:
        print(end)
        break
    else:
        end += 1
