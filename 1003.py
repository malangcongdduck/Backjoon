import sys
n=int(sys.stdin.readline())
ans=[0]*100
ans[0]=0
ans[1]=1
#0과 1의 호출은 입력한 num보다 앞의 수만큼 0과 1이 호출됨
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif ans[n]!=0:
        return ans[n]
    else: 
        ans[n]=fibonacci(n-1)+fibonacci(n-2)
        return ans[n]


result=[]
for i in range(n):
    num=int(sys.stdin.readline())
    fibonacci(num)
    if num==0:
        result.append([1,0])
    else:
        result.append([ans[num-1], ans[num]])

for i in result:
    print(i[0], i[1])
