# try2 - 테스트는 맞으나 정확성 떨어짐
from collections import deque
def solution(maps):
#     global maze, start, lever, end
    map = [list(m) for m in maps]
    n = len(map)
    m = len(map[0])

    for i, lst in enumerate(map):
        if 'S' in lst:
            start = (i, lst.index('S'))
        if 'L' in lst:
            lever = (i, lst.index('L'))
        if 'E' in lst:
            end = (i, lst.index('E'))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(start, end):
        maze = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if map[i][j] != 'X':
                    maze[i][j] = 1
        s_x, s_y = start
        e_x, e_y = end
        queue = deque()
        queue.append((s_x, s_y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # print(nx, ny)

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    # print('범위밖')
                    continue

                if maze[nx][ny] == 0: # X일경우
                    # print('길없음')
                    continue

                if maze[nx][ny] == 1: #start, lever, end일경우
                    maze[nx][ny] = maze[x][y] + 1
                    # print('업데이트')
                    queue.append((nx, ny))
        # print(maze)
        return maze[e_x][e_y]-1 if maze[e_x][e_y] != 1 else -1
    
    result1 = bfs(start, lever)
    result2 = bfs(lever, end)
    return -1 if result1 == -1 or result2 == -1 else result1+result2
# return maze[end[0][0]][end[0][1]]

# maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
maps = ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]
maps = ["SOOOL", "OOOOE"]
solution(maps)