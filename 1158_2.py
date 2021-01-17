#시간초과

import sys
n,k=map(int,sys.stdin.readline().split())
s=[i for i in range(1,n+1)]
ans='<'

#생존자 넣기
while True:
    #k-1명 넘기기
    for i in range(k-1):
        s.append(s.pop(0))

    #k번째 제거
    ans=ans+str(s.pop(0))
    if len(s)==0:
        break
    else:
        ans=ans+', '

print(ans+'>')
