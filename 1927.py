import heapq
import sys

t=int(sys.stdin.readline())
heap=[]

for i in range(t):
    ans=int(sys.stdin.readline())

    if ans==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap))

    else:
        heapq.heappush(heap, ans)