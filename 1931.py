n=int(input())

time=[list(map(int,input().split())) for i in range(n)]
time.sort(key=lambda x:(x[1],x[0]))
#lambda함수: 원래의 함수를 만드는 방식과 달리 이름에 대한 정의 없이 간단하게 만드는 익명의 함수
#x:y y를 기준으로 리턴
#-> sort(key=~~~y) == 이중 리스트에서 y를 기준으로 sort
#-> 적용: 끝나는 시간을 우선으로 정렬, 시간이 같으면 시작하는 시간으로 정렬

count=1
f=time[0][1]
for i in range(1,n):
    if f<=time[i][0]:
        f=time[i][1]
        count+=1

print(count)