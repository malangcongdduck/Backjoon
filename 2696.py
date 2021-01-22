import sys
import heapq

t=int(sys.stdin.readline())
for i in range(t):
    heap_max=[]
    heap_min=[]
    n=int(sys.stdin.readline())
    ans=[]

    for _ in range(n//10+1):
        li=list(map(int,sys.stdin.readline().split()))
        for i in li:
            ans.append(i)

    mid=[]
    #print(ans)

    for j in range(len(ans)):
        if len(heap_max)<=len(heap_min):
            heapq.heappush(heap_max,(-ans[j],ans[j]))
        else:
            heapq.heappush(heap_min,ans[j])

        if heap_min and heap_max[0][1]>heap_min[0]:
            temp1=heapq.heappop(heap_max)[1]
            temp2=heapq.heappop(heap_min)
            heapq.heappush(heap_min,temp1)
            heapq.heappush(heap_max,(-temp2,temp2))

        if (j+1)%2!=0:
            mid.append(heap_max[0][1])

    print(len(mid))
    for k in range(len(mid)):
        if (k+1)%10==0:
            print(mid[k],end='\n')
        else:
            print(mid[k],end=' ')
    
    print()