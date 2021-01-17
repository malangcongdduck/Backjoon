w=input()
time=0
alpha=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

if 2<=len(w)<=15:
    for i in range(len(w)):        
        for j in alpha:
            if w[i] in j:
                time+=(alpha.index(j)+3)

print(time)
