'''
h,m=map(int,input().split())

if h==0:
    h=24

h=h*60
total=h+m-45

total_h=total//60
total_m=total%60
print(total_h,total_m)
'''

h,m=map(int,input().split())

if m>=45:
    print(h,m-45)
elif m<45 and h!=0:
    print(h-1,m+15)
elif m<45 and h==0:
    print(23,m+15)