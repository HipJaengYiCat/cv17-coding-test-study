'''
1 x 1 크기의 칸들로 이루어진 직사각형 격자 형태의 미로에서 탈출하려고 합니다.
각 칸은 통로 또는 벽으로 구성되어 있으며, 벽으로 된 칸은 지나갈 수 없고 통로로 된 칸으로만 이동할 수 있습니다.
통로들 중 한 칸에는 미로를 빠져나가는 문이 있는데, 이 문은 레버를 당겨서만 열 수 있습니다.
레버 또한 통로들 중 한 칸에 있습니다.
따라서, 출발 지점에서 먼저 레버가 있는 칸으로 이동하여 레버를 당긴 후
미로를 빠져나가는 문이 있는 칸으로 이동하면 됩니다. 이때 아직 레버를 당기지 않았더라도
출구가 있는 칸을 지나갈 수 있습니다. 미로에서 한 칸을 이동하는데 1초가 걸린다고 할 때,
최대한 빠르게 미로를 빠져나가는데 걸리는 시간을 구하려 합니다.

미로를 나타낸 문자열 배열 maps가 매개변수로 주어질 때, 미로를 탈출하는데 필요한 최소 시간을
return 하는 solution 함수를 완성해주세요. 만약, 탈출할 수 없다면 -1을 return 해주세요.

1. s,e,l의 좌표를 추출한다.

2. s 부터 l 까지의 경로를 구함

2-1 s 부터 l까지의 경로가 존재하지 않다면 
2-1-1.  -1을 리턴 후 프로그램 종료

2-2 s 부터 l 까지의 경로가 존재한다면
2-2-1 s to l 까지의 거리를 저장한 뒤 l to e까지의 경로 탐색

3-1 위경로가 존재한다면 두 거리를 더한뒤 리턴
3-2 경로가 존재하지 않는 다면 -1을 리턴


'''

from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def solution(maps):
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    coord = {} #시작,레버, 도착지를 저장하는 딕셔너리
    # 시작,도착,레버의 정보 추출, 입력값 그래프로 만들기
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