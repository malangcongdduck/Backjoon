import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()

cnt = Counter(arr).most_common(2)

print(round(sum(arr)/n))
print(arr[int(n/2)])
if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(arr) - min(arr))
