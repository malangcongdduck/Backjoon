import sys
n=int(sys.stdin.readline())
n_list=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
m_list=list(map(int,sys.stdin.readline().split()))

n_list.sort()

for i in m_list:
    first,end=0,n-1
    while first<=end:
        mid=(first+end)//2
        if n_list[mid]==i:
            print('1',end=' ')
            break
        elif n_list[mid]>i:
            end=mid-1
        else:
            first=mid+1
    else:
        print('0',end=' ')   
