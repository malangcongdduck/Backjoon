import sys
n=int(sys.stdin.readline())
n_list=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
m_list=list(map(int,sys.stdin.readline().split()))

n_list.sort()
#print(n_list)

#Upper Bound:찾는값보다 큰 첫번째 위치(초과)를 반환
#Lower Bound:찾는값보다 크거나 같은 첫번째 위치(이상)를 반환
#ex) {1,3,3,5,7}이면 UB=[3] LB=[1] UB-LB=개수
#주의! UB가 리스트의 마지막이면 마지막위치를 반환
def upperBound(li,front,rear,key):
    while front<rear:
        mid=(front+rear)//2
        if li[mid]<=key:
            front=mid+1
        else:
            rear=mid
    return rear

def lowerBound(li,front,rear,key):
    while front<rear:
        mid=(front+rear)//2
        if li[mid]<key:
            front=mid+1
        else:
            rear=mid
    return rear

for i in m_list:
    cnt=0
    first,end=0,n-1
    temp1=upperBound(n_list,first,end,i)
    temp2=lowerBound(n_list,first,end,i)
    if n_list[temp1]==i:
        cnt+=temp1-temp2+1
    else:
        cnt+=temp1-temp2 
    print(cnt,end=' ')
