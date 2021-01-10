import sys
n=int(sys.stdin.readline())
ln=list(range(1,n+1)) #1~n까지의 수
true_p=1
ans=[] #정답리스트
s=[] #스택
for i in range(n):
    ord=int(sys.stdin.readline())

    #안되는경우
    if ln.count(ord)==0 and s[-1]!=ord:
        true_p=0
        continue
    
    #push
    if ln[ord-1]!=0:
        a=ln.index(ord)
        for j in range(a+1):
            if ln[j]!=0:
                s.append(ln[j])
                ans.append('+')
                ln[j]=0
                    
    #pop
    if s.count(ord)!=0:
        for j in range(len(s)):
            temp=s.pop()
            ans.append('-')
            if temp==ord:
                break

    print(ln)
    print(s)
    print(ans)


if true_p==1:
    for i in ans:
        print(i)
else:
    print('NO')