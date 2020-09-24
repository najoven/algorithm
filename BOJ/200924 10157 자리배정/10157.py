import sys; sys.stdin = open('input.txt', 'r')

x, y = map(int, input().split())

N = int(input())
visit = [[0] * y for _ in range(x)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

sx = 0
sy = 0
l = 0
if N > x*y:
    result = 0
    print(result)
else:
    numbers = [i for i in range(1, N+1)]

    for number in numbers:
        visit[sx][sy] = number
        tx = sx + dx[l]
        ty = sy + dy[l]
        if tx < 0 or tx == x or ty < 0 or ty == y or visit[tx][ty] != 0:
            l += 1
            if l == 4:
                l = 0
        if number == N:
            break
        tx = sx + dx[l]
        ty = sy + dy[l]
        sx = tx
        sy = ty

    print(sx + 1, sy + 1)



