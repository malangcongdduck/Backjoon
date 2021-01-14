import sys

li=sys.stdin.readline().split('-')
#print(li)

result=0
#첫번째 식은 더해주기
for i in li[0].split('+'):
    result+=int(i)

for i in li[1:]:
    for j in i.split('+'):
        result-=int(j)

print(result)