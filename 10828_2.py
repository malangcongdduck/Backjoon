import sys
class Stack:
    def __init__(self,capacity):
        self.capacity=capacity
        self.stk=[None]*self.capacity
        self.ptr=0

    def is_empty(self):
        return self.ptr<=0

    def push(self, x):
        self.stk[self.ptr]=x
        self.ptr+=1

    def pop(self):
        if self.is_empty():
            return -1
        else:
            self.ptr-=1
            x=self.stk[self.ptr]
            return x
    
    def peek(self):
        if self.is_empty():
            return -1
        else:
            return self.stk[self.ptr-1]


n=int(sys.stdin.readline())
s=Stack(n+1)
for i in range(n):
    ord=sys.stdin.readline().split()
    
    if ord[0]=='push':
        s.push(int(ord[1]))
    elif ord[0]=='pop':
        print(s.pop())
    elif ord[0]=='size':
        print(s.ptr)
    elif ord[0]=='empty':
        if s.is_empty()==False:
            print('0')
        else:
            print('1')
    else:
        print(s.peek()) 
