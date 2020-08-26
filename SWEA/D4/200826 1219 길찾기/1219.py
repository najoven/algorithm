import sys
sys.stdin = open('input.txt', 'r')

T = 10
N = 100

def DFS_iter(v):
    S = [v]
    visit[0] = 1
    check = []
    while S:
        for w in range(1, N):
            if G[v][w] and not visit[w]:
                visit[w] = 1
                if w == 99:
                    return 1
                S.append(v)
                v = w
                break
        else:
            v = S.pop()
    return 0

def DFS(v):
    visit[v] = 1
    for w in range(1, N):
        if G[v][w] and not visit[w]:
            if w == 99:
                print('99에 도달')
                return 1
            DFS(w)
    return 0


for t in range(1, T+1):
    case, roads = map(int, input().split())
    arr = list(map(int, input().split()))

    G = [[0] * (N) for _ in range(N)]
    visit = [0] * N

    for i in range(0, roads*2, 2):
        u, v = arr[i], arr[i+1]
        G[u][v] = 1

    v = 0
    result = DFS_iter(v)
    print('#{} {}'.format(t, result))



