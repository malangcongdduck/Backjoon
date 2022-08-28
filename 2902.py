import sys
name = list(sys.stdin.readline())
result = []

for i in name:
    if "A" <= i <= "Z":
        result.append(i)

print(''.join(result))
