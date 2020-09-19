import sys; sys.stdin = open('input.txt', 'r')


def dfs(v):
    global cnt
    visit[v] = 1
    cnt += 1
    for w in range(1, V+1):
        if G[v][w] and not visit[w]:
            dfs(w)

V = int(input())
E = int(input())

G = [[0] * (V+1) for _ in range(V+1)]
visit = [0] * (V+1)
for _ in range(E):
    s, e = map(int, input().split())
    G[s][e] = G[e][s] = 1

cnt = 0
dfs(1)
print(cnt-1)