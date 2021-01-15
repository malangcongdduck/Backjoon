import sys
s=sys.stdin.readline()
plag_c=0
plag_d=0
result=[]

for i in range(len(s)):
    if s[i]=='c':
        result.append(26-plag_c)
        plag_c=1
        if s[i+1]=='d':
            plag_c=0
            
    elif s[i]=='d':
        result.append(10-plag_d)
        plag_d=1
        if s[i+1]=='c':
            plag_d=0

#print(result)
re=result[0]
for i in range(1,len(result)):
    re*=result[i]

print(re)