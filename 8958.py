<<<<<<< HEAD
n=int(input())

for i in range(n):
    a=input()
    score=0
    num=1
    for j in range(len(a)):
        if a[j]=="X":
            num=1
        elif a[j]=="O":    
            score+=num
            num+=1
=======
n=int(input())

for i in range(n):
    a=input()
    score=0
    num=1
    for j in range(len(a)):
        if a[j]=="X":
            num=1
        elif a[j]=="O":    
            score+=num
            num+=1
>>>>>>> e0846c0484c6df47787461a9982e06dbe6ae4039
    print(score)