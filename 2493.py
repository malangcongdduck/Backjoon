from collections import deque
import sys

n=int(sys.stdin.readline())
tower=list(map(int,sys.stdin.readline().split()))
q=deque()
ans=[]

for i in range(n):
    while q:
        if q[-1][1]<tower[i]:
            q.pop()
        else:
            ans.append(q[-1][0])
            q.append([i+1,tower[i]])
            break
           
    
    if len(q)==0:
        ans.append(0)
        q.append([i+1,tower[i]])
       
for i in ans:
    print(i,end=' ') 
