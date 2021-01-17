<<<<<<< HEAD
n=int(input())
sum=n #26
l=0

while True:
    n_1=sum//10 #2
    n_2=sum%10 #6
    n_3=(n_1+n_2)%10 #8
    sum=(n_2*10)+n_3 #60+8
    l+=1


    if sum==n:
        print(l)
        break
=======
n=int(input())
sum=n #26
l=0

while True:
    n_1=sum//10 #2
    n_2=sum%10 #6
    n_3=(n_1+n_2)%10 #8
    sum=(n_2*10)+n_3 #60+8
    l+=1
 

    if sum==n:
        print(l)
        break
>>>>>>> e0846c0484c6df47787461a9982e06dbe6ae4039
