import sys; sys.stdin = open('sample_input.txt', 'r')

def DFS(x, y):
    if maze[x][y] == 3:
        return 1
    visit[x][y] = 1
    for l in range(4):
        tx = x + dx[l]
        ty = y + dy[l]
        if not 0 <= tx < N or not 0 <= ty < N: continue
        if visit[tx][ty] or maze[tx][ty] == 1: continue
        if DFS(tx, ty) == 1:
            return 1
    return 0


for tc in range(1, int(input())+1):
    N = int(input())
    maze = []
    x, y = 0, 0
    for j in range(N):
        a = input()
        mmaze = []
        for i in range(N):
            mmaze += [int(a[i])]
            if a[i] == '2':
                x, y = j, i
        maze += [mmaze]

    visit = [[0] * N for _ in range(N)]

    # x, y는 start

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    print('#{} {}'.format(tc, DFS(x,y)))


