class Stack:
    def __init__(self,capacity):
        self.stk=[None]*capacity
        self.ptr=0

    def push(self,value):
        self.stk[self.ptr]=value
        self.ptr+=1

    def pop(self):
        self.ptr-=1
        return self.stk[self.ptr]

if __name__ == "__main__":
    n=int(input())
    s=Stack(n)#스택 생성
    sum_s=0

    for i in range(n):  
        a=int(input())
        
        if a==0:
            temp=s.pop()
        else:
            s.push(a)

    for i in range(s.ptr):
        sum_s+=s.pop()

    print(sum_s)