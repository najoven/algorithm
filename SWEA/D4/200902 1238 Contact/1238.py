import sys; sys.stdin = open('input.txt', 'r')

def bfs(v):
    Q = []

    Q.append(v)
    visited[v] = 1
    while Q:
        v = Q.pop(0)
        for w in range(1, V+1):
            if G[v][w] == 1 and not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1




for tc in range(1, 11):
    E, S = map(int, input().split())
    arr = list(map(int, input().split()))
    V = max(arr)
    G = [[0] * (V+1) for _ in range(V+1)]
    for i in range(0, E, 2):
        s, e = arr[i], arr[i+1]
        G[s][e] = 1


    visited = [0] * (V+1)
    bfs(S)
    maxI = 0
    for i in range(1, V+1):
        if visited[maxI] <= visited[i]:
            maxI = i
    print('#{} {}'.format(tc, maxI))
