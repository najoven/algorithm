import sys; sys.stdin = open('input.txt', 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def tomatoes(x, y):
    global cnt
    visit[x][y] = 1
    for l in range(4):
        tx = x + dx[l]
        ty = y + dy[l]
        if tx < 0 or tx >= N or ty < 0 or ty >= M: continue
        if visit[tx][ty] or G[tx][ty]: continue
        G[tx][ty] = 1
        cnt += 1
        tomatoes(tx, ty)

def bfs(x, y):
    global result
    Q = [(x, y)]
    visit[x][y] = 1

    while Q:
        x, y = Q.pop(0)
        result = max(result, visit[x][y] - 1)
        for l in range(4):
            tx = x + dx[l]
            ty = y + dy[l]
            if tx < 0 or tx >= N or ty < 0 or ty >= M: continue
            if visit[tx][ty] or G[tx][ty]: continue
            G[tx][ty] = 1
            Q.append((tx, ty))
            visit[tx][ty] = visit[x][y] + 1


M, N = map(int, input().split())
visit = [[0] * M for _ in range(N)]

G = [list(map(int, input().split())) for _ in range(N)]
print(G)

signal = 0
zero = 0
for i in range(N):
    for j in range(M):
        if G[i][j] == 1:
            x, y = i, j
        elif G[i][j] == 0:
            zero = 1


if zero == 0:
    result = 0
else:
    result = 0
    bfs(x, y)
    signal = 0
    for i in range(N):
        for j in range(M):
            if G[i][j] == 0:
                result = -1
                signal = 1
                break
        if signal == 1:
            break

print(G)
print(visit)
print(result)