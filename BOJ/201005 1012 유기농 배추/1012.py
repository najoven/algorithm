import sys; sys.stdin = open('input.txt', 'r')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bugs(x, y):
    Q.append((x, y))
    visit[x][y] = 1
    while Q:
        x, y = Q.pop(0)
        for l in range(4):
            tx = x + dx[l]
            ty = y + dy[l]
            if 0 > tx or tx >= N or 0 > ty or ty >= M: continue
            if visit[tx][ty] or not farm[tx][ty]: continue
            visit[tx][ty] = 1
            Q.append((tx, ty))

for tc in range(1, int(input()) + 1):
    M, N, K = map(int, input().split())

    farm = [[0] * M for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    for _ in range(K):
        j, i = map(int, input().split())
        farm[i][j] = 1

    Q = []
    cnt = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and not visit[i][j]:
                bugs(i, j)
                cnt += 1

    print(cnt)
