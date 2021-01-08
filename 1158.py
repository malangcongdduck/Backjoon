#시간초과

import sys
class Queue:
    def __init__(self, capacity):
        self.no=0
        self.front=0
        self.rear=0
        self.capacity=capacity
        self.que=[None]*capacity

    def enque(self,x):
        self.que[self.rear]=x
        self.no+=1
        self.rear=(self.rear+1)%self.capacity

    def deque(self):
        x=self.que[self.front]
        self.no-=1
        self.front=(self.front+1)%self.capacity
        return x
    
    def Empty(self):
        return 1 if self.front==self.rear else 0


n,k=map(int,sys.stdin.readline().split())
q=Queue(n+1)
ans='<'

#생존자 넣기
for i in range(1,n+1):
    q.enque(i)

while True:
    #k-1명 넘기기
    for i in range(k-1):
        q.enque(q.deque())

    #k번째 제거
    ans=ans+str(q.deque())
    if q.Empty()==1:
        break
    else:
        ans=ans+', '

print(ans+'>')

