import sys; sys.stdin = open('input.txt', 'r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def section(x, y, color):
    Q.append((x, y))
    visit[x][y] = 1
    while Q:
        x, y = Q.pop(0)
        for l in range(4):
            tx = x + dx[l]
            ty = y + dy[l]
            if tx < 0 or tx >= N or ty < 0 or ty >= N: continue
            if visit[tx][ty] == 1 or colors[tx][ty] != color: continue
            visit[tx][ty] = 1
            Q.append((tx,ty))


def sectionrg(x, y, color):
    visit[x][y] = 1
    Q.append((x, y))
    while Q:
        x, y = Q.pop(0)
        for l in range(4):
            tx = x + dx[l]
            ty = y + dy[l]
            if tx < 0 or tx >= N or ty < 0 or ty >= N: continue
            if visit[tx][ty] == 1: continue
            if (color == 'R' or color == 'G') and colors[tx][ty] == 'B': continue
            elif color == 'B' and colors[tx][ty] != 'B': continue
            visit[tx][ty] = 1
            Q.append((tx, ty))


N = int(input())
colors = []
for _ in range(N):
    colors += [list(input())]
visit = [[0] * N for _ in range(N)]

Q = []
cnt1 = 0
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            section(i, j, colors[i][j])
            cnt1 += 1


visit = [[0] * N for _ in range(N)]
Q = []
cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            sectionrg(i, j, colors[i][j])
            cnt2 += 1

print(cnt1, cnt2)