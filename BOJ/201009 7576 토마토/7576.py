import sys; sys.stdin = open('input.txt', 'r')
from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(Q):
    global result
    global count
    for q in Q:
        x, y = q
        visit[x][y] = 1
    while Q:
        x, y = Q.popleft()
        # 번갈아 뽑게 됨
        count += 1
        result = max(result, visit[x][y] - 1)
        for l in range(4):
            tx = x + dx[l]
            ty = y + dy[l]
            if tx < 0 or tx >= N or ty < 0 or ty >= M: continue
            if visit[tx][ty] or G[tx][ty]: continue
            Q.append([tx, ty])
            visit[tx][ty] = visit[x][y] + 1


M, N = map(int, input().split())

signal = 0
Q = deque()
G = []
visit = []



count = 0
for i in range(N):
    G += [list(map(int, input().split()))]
    visit += [[0] * M]

    for j in range(M):
        if G[i][j] == 1:
            Q.append([i,j])
        elif G[i][j] == -1:
            count += 1


result = 0

bfs(Q)

if count != N*M:
    result = -1

print(result)