import sys
t=int(input())

for i in range(t):
    ins=list(input())
    
    s=[]
    for j in ins:
        s.append(j)

        if j==')':
            if len(s)>1:
                s.pop()
                s.pop()
            else:
                break

    if len(s)==0:
        print('YES')   
    else:
        print('NO')
