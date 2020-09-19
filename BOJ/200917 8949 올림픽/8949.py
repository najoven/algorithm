import sys; sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
scores = [0] * N
sortscores = [0] * N

for i in range(N):
    scores[i] = (1000000**2) * arr[i][1] + (1000000) * arr[i][2] + arr[i][3]
    sortscores[i] = (1000000**2) * arr[i][1] + (1000000) * arr[i][2] + arr[i][3]


sortscores.sort(reverse=True)
result = []
for s in sortscores:
    if s not in result:
        result.append(s)
final = [0] * N
cnt = 0
signal = 0
cnt = 1
for r in result:
    subcnt = 0
    for i in range(N):
        if r == scores[i]:
            final[i] = cnt
            subcnt += 1
            if arr[i][0] == K:
                signal = 1
                break
    cnt += subcnt
    if signal == 1:
        break

print(final[i])




