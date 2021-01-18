import sys
from collections import deque

s=sys.stdin.readline()
stack=deque()
ans=[]

for i in s:
    if i=='(':
        stack.append(i)
    elif i=='*' or i=='/':
        while stack:
            if stack[-1]=='*' or stack[-1]=='/':
                ans.append(stack.pop())
            else:
                break
        stack.append(i)
    elif i=='+' or i== '-':
        while stack:
            if stack[-1]=='*' or stack[-1]=='/' or stack[-1]=='+' or stack[-1]=='-': 
                ans.append(stack.pop())
            else: break

        stack.append(i)
    elif i==')':
        while True:
            temp=stack.pop()
            if temp=='(':
                break
            else:
                ans.append(temp)
    else:
        ans.append(i)

while stack:
    ans.append(stack.pop())

for i in ans:
    if i!='\n':
        print(i,end='')