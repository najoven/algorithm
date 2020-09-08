import sys; sys.stdin = open('input.txt', 'r')


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def DFS(x, y):
    global cnt
    for l in range(4):
        tx, ty = x + dx[l], y + dy[l]
        if 0 > tx or tx >= N or 0 > ty or ty >= N: continue
        if arr[tx][ty] - arr[x][y] == 1:
            cnt += 1
            visit[arr[tx][ty]] = 1
            DFS(tx, ty)


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * (N*N + 1)
    result = [0] * (N*N + 1)
    ans = 0
    coor = N*N
    for i in range(N):
        for j in range(N):
            if arr[i][j] < N*N and not visit[arr[i][j]]:
                visit[arr[i][j]] = 1
                cnt = 1
                DFS(i, j)
                result[arr[i][j]] = cnt

    ans = 0
    coor = 0
    for i in range(len(result)):
        cnt = result[i]
        if cnt > ans:
            ans = cnt
            coor = i

    print('#{} {} {}'.format(tc, coor, ans))

