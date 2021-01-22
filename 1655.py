import sys
import heapq

n=int(sys.stdin.readline())
heap_max=[]
heap_min=[]

for i in range(n):
    ans=int(sys.stdin.readline())
    
    if len(heap_max)<=len(heap_min):
        heapq.heappush(heap_max,(-ans,ans))
    else:
        heapq.heappush(heap_min,ans)

    if heap_min and heap_max[0][1]>heap_min[0]:
        temp1=heapq.heappop(heap_max)[1]
        temp2=heapq.heappop(heap_min)
        heapq.heappush(heap_min,temp1)
        heapq.heappush(heap_max,(-temp2,temp2))


    #print(heap_min)
    #print(heap_max)
    print(heap_max[0][1])