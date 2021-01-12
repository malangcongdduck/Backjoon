import sys
m=int(sys.stdin.readline())
n=int(sys.stdin.readline())

list_mn=[]
for i in range(m,n+1):
    true_p=1
    if i==1:
        continue

    for j in range(2,i):
        if i%j==0:
            true_p=0
            break
    if true_p==1:
        list_mn.append(i)

#print(list_mn)
if len(list_mn)==0:
    print('-1')
else:
    print(sum(list_mn))
    print(min(list_mn))