import sys; sys.stdin = open('input.txt', 'r')

def DFS(v):
    visit[v] = 1
    for w in range(1, V+1):
        if G[v][w] == 1:
            counting[w] -= 1
            if counting[w] == 0:
                print(w, end=' ')
                DFS(w)


for tc in range(1, 11):

    print('#{}'.format(tc), end =' ')
    V, E = map(int, input().split())
    paths = list(map(int, input().split()))

    G = [[0] * (V+1) for _ in range(V+1)]
    counting = [0] * (V+1)
    visit = [0] * (V+1)
    for i in range(E):
        G[paths[i*2]][paths[i*2+1]] = 1
        counting[paths[i*2+1]] += 1

    for i in range(1, V+1):
        if counting[i] == 0 and not visit[i]:
            print(i, end =' ')
            DFS(i)

    print()


