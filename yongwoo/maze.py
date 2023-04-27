from collections import deque
import copy

maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]

#boundary
n = len(maps[0])
m = len(maps)

#making graph
graph1 = [[] for _ in range(len(maps))]
for i in range(m):
    for idx, j in enumerate(maps[i]):
        if j == 'S':
            graph1[i].append(1)
            start = (i, idx)
        if j == 'E':
            graph1[i].append(1)
            exit = (i, idx)
        if j == 'L':
            graph1[i].append(1)
            lever = (i, idx)
        if j == 'O':
            graph1[i].append(1)
        if j == 'X':
            graph1[i].append(0)

graph2 = copy.deepcopy(graph1)

#bfs
def bfs(start_point, end_point, graph):
    queue = deque(())
    queue.append((start_point))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= m or ny <= -1 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            elif nx == end_point[0] and ny == end_point[1]:
                return graph[x][y]
            elif graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return -1

startn = bfs(start, lever, graph1)
levern = bfs(lever, exit, graph2)
if startn == -1 or levern == -1:
    print(-1)
else:
    print(startn+levern)