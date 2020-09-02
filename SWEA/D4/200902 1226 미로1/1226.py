import sys; sys.stdin = open('input.txt', 'r')


def BFS(x, y):
    Q = [[x,y]]

    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 > tx or N <= tx or 0 > tx or N <= ty: continue
            if G[tx][ty] == 1 or visit[tx][ty] == 1: continue
            if G[tx][ty] == 3: return 1
            Q.append((tx, ty))
            visit[tx][ty] = 1
    return 0


def Start(N):
    for i in range(N):
        for j in range(N):
            if G[i][j] == 2:
                sx = i
                sy = j
                return sx, sy


for _ in range(1, 11):
    tc = int(input())
    N = 16

    G = [[] for _ in range(N)]

    for i in range(N):
        for j in (input()):
            G[i] += [int(j)]


    x, y = Start(N)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visit = [[0] * N for _ in range(N)]
    print('#{} {}'.format(tc, BFS(x, y)))
