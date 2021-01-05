<<<<<<< HEAD
def eq_se(n):
    if n<100:
        return True
    a=n//100
    b=n//10%10
    c=n%10
    return a+c==2*b

n=int(input())

count=0
for i in range(1, n+1):
    if eq_se(i):
        count+=1

=======
def eq_se(n):
    if n<100:
        return True
    a=n//100
    b=n//10%10
    c=n%10
    return a+c==2*b

n=int(input())

count=0
for i in range(1, n+1):
    if eq_se(i):
        count+=1

>>>>>>> e0846c0484c6df47787461a9982e06dbe6ae4039
print(count)