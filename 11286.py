import sys
import heapq

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
        if ans<0:
            heapq.heappush(heap,(-ans,ans))
        else:
            heapq.heappush(heap,(ans,ans))