from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def solution(maps):
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    coord = {}
    for i,ele in enumerate(maps):
        maps[i] = list(ele)
        for idx,e in enumerate(ele):
            if e == "S":
                coord["srt"] = [i,idx]
            elif e =="E":
                coord["exit"] = [i,idx]
            elif e == "L":
                coord["lever"] = [i,idx]
    def BFS(srt,target):
        q = deque([srt])
        visited[srt[0]][srt[1]] = 1
        while q:
            x,y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(maps) and 0 <= ny <len(maps[0]):
                    if maps[nx][ny] != "X" and not visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append([nx,ny])
                    
                        if maps[nx][ny] == target:
                            # print(visited[nx][ny])
                            return visited[nx][ny]-1
        return None
    SToL = BFS(coord["srt"],"L")
    if not SToL:
        return -1
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    
    LToE = BFS(coord["lever"],"E")
    if not LToE:
        return -1
    return SToL+LToE