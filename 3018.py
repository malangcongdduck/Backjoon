#미완성
import sys
from collections import deque

n=int(sys.stdin.readline())
e=int(sys.stdin.readline())
q=deque()
ans=[]
for i in range(e):
    today=list(map(int,sys.stdin.readline().split()))

    for j in range(1,today[0]+1):
        #선영이가 참여한 날
        #New 노래니까 참여자 스택에 넣기
        if today.count(1)>=1:
            if today[j] not in q:
                q.append(today[j])

        #선영이가 참여하지 않은 날
        #동기화니까 스택에서 빼버리기
        else:
            if today[j] in q: 
                q.remove(today[j])

    #print(q)

#스택에 있는 사람들이 모든 노래를 아는 것
for i in q:
    ans.append(i)

ans.sort()
for i in ans:
    print(i)

'''반례
4
2
3 1 2 4
2 1 3

=> 1
'''