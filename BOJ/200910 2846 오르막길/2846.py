import sys; sys.stdin = open('input.txt', 'r')

N = int(input())

roads = list(map(int, input().split()))

visit = [0] * N
ans = 0
result = []
for i in range(N-1):
    if not visit[i] and roads[i] < roads[i+1]:
        visit[i] = 1
        s = i
        while i < N-1:
            if roads[i] < roads[i+1]:
                visit[i+1] = 1
                i += 1
                e = i
            else:
                e = i
                break
        result.append([s, e])


diff = []
ans = 0
for r in result:
    ans = max(ans, roads[r[1]]-roads[r[0]])

print(ans)