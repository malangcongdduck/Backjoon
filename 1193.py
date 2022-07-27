import sys

n = int(sys.stdin.readline())

line = 0
end = 0

while n > end:
    line += 1
    end += line

end_diff = end - n

if line % 2 == 1:
    top = end_diff + 1
    bottom = line - end_diff
else:
    top = line - end_diff
    bottom = end_diff + 1

print(f'{top}/{bottom}')
