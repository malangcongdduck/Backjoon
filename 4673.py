def d(n):
    gn=list(map(int, str(n)))#n을 str로 만들어 list에 int형으로 넣음
    return n+sum(gn)

gen=[]

for i in range(10000):
    gen.append(d(i))

    if i not in gen:
        print(i)
