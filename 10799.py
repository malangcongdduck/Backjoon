from collections import deque
import sys

li=list(sys.stdin.readline())
s=deque()
stick=0

for i in range(len(li)):
    #열린괄호(막대기&레이저)
    if li[i]=='(':
        s.append('(')
    #닫힌괄호(레이저)
    elif li[i]==')' and li[i-1]=='(':
        s.pop()
        stick+=len(s)
    #닫힌괄호(막대기)
    elif li[i]==')' and s[-1]=='(':
        s.pop()
        stick+=1

    #print(i+1, s)
    #print(stick)

print(stick)