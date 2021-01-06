a,b,c=map(int,input().split())

if b>=c: #손익분기점이 존재하지 않음
    print("-1")
else:
    n=a//(c-b)+1 #0원은 수익이 아니니까 1을 더해줘야함
    print(n)
        