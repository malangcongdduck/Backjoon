import sys

n = int(sys.stdin.readline())
ropes = [0] * n

for i in range(n):
    ropes[i] = int(sys.stdin.readline())

weight = sorted(ropes)

# 오름차순 기준으로 로프 개수 * 해당 로프 최대 중량
# 로프 2개일 때 [10*2, 15*1]
for i in range(n):
    weight[i] = weight[i] * (n - i)

print(max(weight))
