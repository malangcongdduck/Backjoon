x=int(input())
ans=[0]*10 #Stack

ans[0]=64 #스택에 64넣어서 시작
ptr=1 #스택 포인터


if sum(ans)>x:
    #i=1
    while True:
        #pop과정
        ptr-=1
        temp=ans[ptr]
        
        #push과정
        #1. 짧은것 절반 자르기
        temp_2=temp//2
        ans[ptr]=temp_2
        ptr+=1

        #2. 합이 크거나 같으면 하나 버리기==스택에 넣지 않음
        #==합이 작으면 스택에 넣어서 keep 하기

        if sum(ans)<x: #스택에 넣어서 keep
            ans[ptr]=temp_2
            ptr+=1
            #print(f'{i}. {ans}')
        elif sum(ans)==x: #합이 같으면 break
            print(ptr)
            #print(f'{i}. {ans}')
            break
        else: #스택에 넣지 않고 버리기
            #print(f'{i}. {ans}')
            pass
        #i+=1

elif sum(ans)==x:
    print(ptr)