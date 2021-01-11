from collections import deque
import sys

t=int(sys.stdin.readline()) #테스트케이스 수

for i in range(t):
    n,m=map(int,sys.stdin.readline().split())
    s=list(map(int,sys.stdin.readline().split()))
    #s_copy=[i for i in s]

    #중요도 문서 삽입
    q=deque()
    for j in s:
        q.append(j)

    cnt=0
    target=q[m]
    s[m]='*'#q 문서의 타겟
    while True:
        #print(q)
        #print(s)

        if max(q)==q[0]:
            temp=q.popleft()
            doc_check=s.pop(0)
            cnt+=1
            if temp==target and doc_check=='*':
                print(cnt)
                break
        else:
            q.append(q.popleft())
            s.append(s.pop(0))