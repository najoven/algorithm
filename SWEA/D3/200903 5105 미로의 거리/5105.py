import sys; sys.stdin = open('sample_input.txt', 'r')

def BFS(x, y):
    Q= [(x, y)]
    visited[x][y] = 1
    while Q:
        x, y = Q.pop(0)
        if G[x][y] == '3': return visited[x][y] - 2
        for l in range(4):
            tx = x + dx[l]
            ty = y + dy[l]
            if tx < 0 or tx >= N or ty < 0 or ty >= N: continue
            if G[tx][ty] == '1' or visited[tx][ty] != 0: continue
            Q.append((tx, ty))
            visited[tx][ty] = visited[x][y] + 1
    return 0


for tc in range(1, int(input())+1):
    N = int(input())

    G = [input() for _ in range(N)]

    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if G[i][j] == '2':
                x, y = i, j

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[0] * N for _ in range(N)]
    print('#{} {}'.format(tc, BFS(x, y)))
