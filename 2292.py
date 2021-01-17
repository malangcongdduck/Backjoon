n = int(input())
count = 2

i = 1
while True:
    if n == 1:
        print("1")
        break
    if n >=(3*i*i-3*i+1) and n <= (3*(i+1)*(i+1)- 3*(i+1)+1):
        print(count)
        break
    else:
        count += 1
        i += 1 
