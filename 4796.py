import sys

case=0
while True:
    case+=1
    l,p,v=map(int,sys.stdin.readline().split())

    if l+p+v==0:
        break
    else:
        result=(v//p)*l+min(l,v-p*(v//p))
        print(f'Case {case}: {result}') 
