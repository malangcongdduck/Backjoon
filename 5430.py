import sys
t=int(sys.stdin.readline())

for i in range(t):
    ord=sys.stdin.readline()
    n=int(sys.stdin.readline())
    s=sys.stdin.readline()[1:-2].split(",")
    true_p=1
    flag=0 #0이면 왼쪽 1이면 오른쪽

    for p in ord:
        if p=='R':
            if flag==0: flag=1
            elif flag==1: flag=0
        elif p=='D':
            if len(s)==0 or n==0:
                true_p=0
                break
            else:
                if flag==0: s.pop(0)
                elif flag==1: s.pop()

    if ord.count('R')%2!=0:
        s.reverse()

    if true_p==0:
        print('error')
    elif (true_p==1 and n==0) or (true_p==1 and len(s))==0:
        print('[]')
    elif true_p==1 and len(s)!=0:
        print('[',end='')
        for i in range(len(s)-1):
            print(s[i],end=',')
        print(s[-1],end='')
        print(']')
