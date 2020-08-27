import sys
sys.stdin = open('sample_input.txt', 'r')

def DFS(v):
    stack = [v]
    visit[0] = 1
    check = []
    while stack:
        for w in range(1, V+1):
            if paths[v][w] and not visit[w]:
                visit[w] = 1
                if w == G:
                    return 1
                stack.append(v)
                v = w
                break
        else:
            v = stack.pop()
    return 0


T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    paths = [[0] * (V+1) for _ in range(V+1)]
    visit = [0] * (V+1)

    for _ in range(E):
        go, depart = map(int, input().split())
        paths[go][depart] = 1

    S, G = map(int, input().split())

    w = 0
    print('#{} {}'.format(t, DFS(S)))

