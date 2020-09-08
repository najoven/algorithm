import sys; sys.stdin = open('s_input.txt', 'r')


def DFS(v):
    visit[v] = 1
    for w in range(1, N+1):
        if G[v][w] and not visit[w]:
            DFS(w)

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    G = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        G[s][e] = G[e][s] = 1

    visit = [0] * (N+1)

    cnt = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if not visit[j]:
                DFS(j)
                cnt += 1

    print('#{} {}'.format(tc, cnt))
