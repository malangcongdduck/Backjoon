while True:
    ins=input()
    s=[] #스택 생성
    true_p=1

    for i in ins:
        if i=='.':
            break
        elif i=='(' or i=='[':
            s.append(i)
        elif i==')':
            if len(s)!=0 and s[len(s)-1]=='(':
                s.pop()
            else:
                true_p=0
        elif i==']':
            if len(s)!=0 and s[len(s)-1]=='[':
                s.pop()
            else:
                true_p=0
        else:
            pass

    if ins=='.':
        break
    elif true_p==1 and len(s)==0:
        print('yes')
    else:
        print('no') 
