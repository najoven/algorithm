import sys; sys.stdin = open('sample_input.txt', 'r')

def BFS(v):
    Q = []

    Q.append(v)
    visit[v] = 1
    while Q:
        v = Q.pop(0)
        if v == G: return visit[v] - 1
        for w in range(1, V+1):
            if visit[w] != 0 or arr[v][w] != 1: continue
            Q.append(w)
            visit[w] = visit[v] + 1
    return 0


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())

    arr = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        s, e = map(int, input().split())
        arr[s][e] = arr[e][s] = 1
    S, G = map(int, input().split())
    visit = [0] * (V + 1)
    print('#{} {}'.format(tc, BFS(S)))