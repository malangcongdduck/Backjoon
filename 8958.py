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
    print(score)