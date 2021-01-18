t=int(input())

for i in range(t):
    ins=input()
    s=[]
    for j in ins:
        if len(s)>=1:
            if j=='(':
                s.append(j)
            else:
                if s[len(s)-1]=='(':
                    s.pop()
                else:
                    s.append(j)
        else:
            s.append(j)


    if len(s)==0:
        print('YES')   
    else:
        print('NO')
