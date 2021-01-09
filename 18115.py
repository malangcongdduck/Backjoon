from collections import deque

n=int(input())
dq=deque()

#명령어 리스트
ans=list(map(int,input().split()))
ans.reverse()

for i in range(n):
    if ans[i]==1:
        dq.appendleft(i+1)
    elif ans[i]==2:
        temp=dq.popleft()
        dq.appendleft(i+1)
        dq.appendleft(temp)
    else:
        dq.append(i+1)

for i in dq:
    print(f'{i} ',end='')