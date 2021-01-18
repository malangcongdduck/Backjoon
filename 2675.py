t=int(input())

for i in range(t):
    r,s=map(str,input().split())
    r=int(r)

    for i in range(len(s)):
        print(f'{s[i]*r}',end='')
    
    print()
