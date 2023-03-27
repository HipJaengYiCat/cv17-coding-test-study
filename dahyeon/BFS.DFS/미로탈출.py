## 시도 1 => 30.4
from collections import deque 
def solution(maps):
    lever = False # 레버를 당겼는가
    end = False #끝지점 도달 (반환값을 위한 변수)
    dx = [0,0,-1,1]
    dy = [-1,1,0,0] #좌,우,상,하
    a,b = [-1,-1]
    q = deque() 
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    #(0,0)에서 시작이 아님 시작 위치 찾기
    for i in range(len(maps)):
        if 'S' in maps[i]:
            x = i
            y = maps[i].index('S')
    print(x,y)   
    q.append((x,y))
    
    while q: 
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny] != "X" and not visited[nx][ny]: #맵 안에 존재하고 벽이 아니고, 방문하지 않았다면
                if maps[nx][ny] == "L": #만약 레버에 도착한다면
                    lever = True #레버를 당겨주자
                
                if maps[nx][ny] == "E" and lever : #끝지점에 도착했으며 lever가 당겨진 상태라면
                    end = True #도착
                    visited[nx][ny] = visited[x][y] + 1
                    a,b = nx,ny
                    print(a,b, visited[a][b])
                    break
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
                
    print(lever,end,visited)    
        
    if end :
        return visited[a][b]
    else:
        return -1

"""
S : 시작
E : 끝
L : 레버 
S->L->E 순서대로 이동해야함
==> 여러 번 지나갈 수 있음 주의................
==> 시작점부터 레버까지 간 다음 visited 초기화가 필요함

+ 레버를 중간에 당겨야하므로 레버 당김 여부가 필요함

"""

## 시도 2
from collections import deque 
def solution(maps):
    answer = 0
    lever = False # 레버를 당겼는가
    dx = [0,0,-1,1]
    dy = [-1,1,0,0] #좌,우,상,하
    
    q = deque() 
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    #(0,0)에서 시작이 아님 시작 위치 찾기
    for i in range(len(maps)):
        if 'S' in maps[i]:
            x = i
            y = maps[i].index('S')  
    q.append((x,y))
    
    while q: 
        x,y = q.popleft()
        if maps[x][y] == "L" and not lever: #만약 레버에 처음 도착한다면
                    lever = True #레버를 당겨주자
                    answer += visited[x][y] #시작점부터 레버까지 시간 더해주기
                    q = deque()
                    q.append((x,y)) #이번엔 레버가 시작점이 되는 것
                    visited = [[0]*len(maps[0]) for _ in range(len(maps))] # 모두 초기화..
                    continue
        if maps[x][y] == "E" and lever : #끝지점에 도착했으며 lever가 당겨진 상태라면
                    answer += visited[x][y] #레버부터 끝점까지
                    return answer         
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny] != "X" and not visited[nx][ny]: #맵 안에 존재하고 벽이 아니고, 방문하지 않았다면
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
                
    return -1


"""
S : 시작
E : 끝
L : 레버 
S->L->E 순서대로 이동해야함
+ 레버를 중간에 당겨야하므로 레버 당김 여부가 필요함
==> 여러 번 지나갈 수 있음 주의.............
==> 여러 번 지나갈 수 있다 & 최소 시간 => 결국 중복 금지는 유지하되, 특정 상황에서만 최소로 중복 허용해주는 것
==> 즉, 시작점부터 레버까지 간 다음 visited 초기화가 필요함
ans = (시작->레버) + (레버->마지막)

"""
