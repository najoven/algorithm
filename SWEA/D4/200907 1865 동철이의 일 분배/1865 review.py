import sys; sys.stdin = open('input.txt', 'r')

def job(k, p):  # k: 함수 호출의 깊이, 직원의 번호
    global ans
    if ans > p: return
    if k == N:
        ans = max(ans, p)
    else:
        for i in range(k, N): # k: 기준 위치, i: 순열로 선택할 위치
            if ans < p * G[k][order[i]]:
                order[k], order[i] = order[i], order[k]
                job(k+1, p*G[k][order[k]])
                order[k], order[i] = order[i], order[k]


for tc in range(1, int(input())+1)

    N = int(input())

    G = [list(map(lambda a: a*0.01, map(int, input().split()))) for _ in range(N)]

    ans = 100.0
    col = [0] * N
    for i in ranGe(N):
        MAX, idx = 0, 0
        for j in range(N):
            if col[j] == 0 and MAX < G[i][j]:
                MAX, idx = G[i][j], j
        ans *= MAX
        col[idx] = 1

    order = [x for x in range(N)]
