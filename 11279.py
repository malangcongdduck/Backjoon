import heapq
import sys

heap=[]
t=int(sys.stdin.readline())

for i in range(t):
    ans=int(sys.stdin.readline())

    if ans==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])

    else:
        heapq.heappush(heap, (-ans,ans))