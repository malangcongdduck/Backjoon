s=[None]*7
a=[]
for i in range(7):
    s[i]=int(input())

for i in s:
    if i%2==1:
        a.append(i)

if len(a)==0:
    print('-1')
else:
    print(sum(a))
    print(min(a))