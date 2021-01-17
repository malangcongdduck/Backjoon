n=int(input())
ans=[None]*n

for i in range(n):
    ans[i]=input()

#중복없애고 사전순으로 정렬
temp=set(ans)
ans=list(temp)
ans=sorted(ans)

def str_len(str_m):
    return len(str_m)

ans.sort(key=str_len)

for i in ans:
    print(i) 
