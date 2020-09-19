import sys; sys.stdin = open('input.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    visit[x][y] = 1
    cnt += 1
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 > tx or tx >= N or ty < 0 or ty >= N: continue
        if visit[tx][ty] or G[tx][ty] == '0': continue
        dfs(tx, ty)



N = int(input())
G = []
visit = [[0] * N for _ in range(N)]
for _ in range(N):
    G += list(map(str, input().split()))

houses = []
towns = 0
for i in range(N):
    for j in range(N):
        if G[i][j] == '1' and not visit[i][j]:
            towns += 1
            cnt = 0
            dfs(i, j)
            houses.append(cnt)

houses.sort()

print(towns)
for i in houses:
    print(i)