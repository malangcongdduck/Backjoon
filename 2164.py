from collections import deque
import sys

n=int(sys.stdin.readline())
q=deque()

for i in range(1,n+1):
    q.append(i)

while True:
    if len(q)==1:
        break
    else:
        #1.위에 한장 버림
        q.popleft()
        #2.다음 제일 위 카드를 제일 아래로
        q.append(q.popleft())

    #print(q)

print(q[0]) 
