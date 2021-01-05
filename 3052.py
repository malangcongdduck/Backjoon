a=[None]*10
for i in range(10):
    n=int(input())
    a[i]=n%42

a=set(a)#집합, 순서가 상관 없고, 중복이 허용되지 않는 자료형
print(len(a))
