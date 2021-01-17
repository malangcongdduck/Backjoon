<<<<<<< HEAD
import sys

xx=[-1,1,0,0,-1,1,1,-1]#서,동,남,북,남서,북동,동남,북서
yy=[0,0,-1,1,-1,1,-1,1]
def dfs(x, y):
    global w
    global h
    global G
    #global cnt

    for i in range(8):
        if w>x+xx[i]>=0 and h>y+yy[i]>=0:
            #print(f'G[{y+yy[i]}][{x+xx[i]}]]')
            if G[y+yy[i]][x+xx[i]]==1:
                #print(f'G [{y+yy[i]}][{x+xx[i]}] {cnt} (dfs)')
                G[y+yy[i]][x+xx[i]]=2
                dfs(x+xx[i],y+yy[i])

while True:
    w,h=map(int,sys.stdin.readline().split())#너비,높이
    if w==0 and h==0:
        break

    #그래프 생성
    G=[[0]*w for _ in range(h)]

    for i in range(h):
        ans=sys.stdin.readline().split()
        for j in range(w):
            G[i][j]=int(ans[j])

    #print(G)

    cnt=0
    for i in range(h):
        for j in range(w):
            if G[i][j]==1:
                cnt+=1
                G[i][j]=2
                #print(f'G [{i}][{j}] {cnt} (main)')
                dfs(j,i)


=======
import sys

xx=[-1,1,0,0,-1,1,1,-1]#서,동,남,북,남서,북동,동남,북서
yy=[0,0,-1,1,-1,1,-1,1]
def dfs(x, y):
    global w
    global h
    global G
    #global cnt

    for i in range(8):
        if w>x+xx[i]>=0 and h>y+yy[i]>=0:
            #print(f'G[{y+yy[i]}][{x+xx[i]}]]')
            if G[y+yy[i]][x+xx[i]]==1:
                #print(f'G [{y+yy[i]}][{x+xx[i]}] {cnt} (dfs)')
                G[y+yy[i]][x+xx[i]]=2
                dfs(x+xx[i],y+yy[i])

while True:
    w,h=map(int,sys.stdin.readline().split())#너비,높이
    if w==0 and h==0:
        break

    #그래프 생성
    G=[[0]*w for _ in range(h)]

    for i in range(h):
        ans=sys.stdin.readline().split()
        for j in range(w):
            G[i][j]=int(ans[j])

    #print(G)

    cnt=0
    for i in range(h):
        for j in range(w):
            if G[i][j]==1:
                cnt+=1
                G[i][j]=2
                #print(f'G [{i}][{j}] {cnt} (main)')
                dfs(j,i)


>>>>>>> 80e37cb62920959113c25e45b91cf03610c0231f
    print(cnt)