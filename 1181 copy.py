n=int(input())
ans=[None]*n

for i in range(n):
    ans[i]=input()

#중복없애고 사전순으로 정렬
temp=set(ans)
ans=list(temp)
ans=sorted(ans)

#선택정렬
for i in range(len(ans)-1):
    min=i
    for j in range(i+1,len(ans)):
        if len(ans[min])>len(ans[j]):
            min=j
    ans[i],ans[min]=ans[min],ans[i]


for i in ans:
    print(i)