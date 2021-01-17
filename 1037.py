a=int(input())
s=list(map(int,input().split()))
s.sort()

result=s[0]*s[-1] 
print(result)
