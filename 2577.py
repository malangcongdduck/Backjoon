a=int(input())
b=int(input())
c=int(input())

result=list(str(a*b*c))

for i in range(10):
    print(result.count(str(i)))#i를 문자열로 바꿔서 result안에 i와 같은 것을 count
