from collections import deque
import copy
def dfs(start,end,maps):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    len1=len(maps[0])
    visited=[[False]*len1 for _ in range(len(maps))] #처음에 30점 맞은 이유1
    queue=deque()
    
    for i in range(len(maps)):
        for j in range(len1):
            if maps[i][j]==start:
                maps[i][j]=0
                visited[i][j]=True #처음에 30점 맞은 이유1
                queue.append((i,j))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=len(maps) or ny>=len(maps[0]):#처음에 30점 맞은 이유2 x,y 인덱스 range 바뀜
                continue
            if maps[nx][ny]==end: # end에 도달하면
                return maps[x][y]+1
            elif maps[nx][ny]!='X' and not visited[nx][ny]: 
                #처음에 30점 맞은 이유2 'O'일때만 고려하면 안됨 X가 아닌 모든 경우 고려해야함
                maps[nx][ny]=maps[x][y]+1
                visited[nx][ny]=True
                queue.append((nx,ny))
    return -1
    
def solution(maps):
    for i in range(len(maps)):
        maps[i]=list(maps[i])
    maps2=copy.deepcopy(maps) #처음에 30점 맞은 이유3 maps 값 바뀌면 E가 사라짐..
    n1=dfs('S','L',maps)
    n2=dfs('L','E',maps2)
    if n1==-1 or n2==-1:
        return -1
    else:
        return n1+n2
        