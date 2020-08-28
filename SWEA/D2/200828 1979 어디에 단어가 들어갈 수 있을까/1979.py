import sys; sys.stdin = open('input.txt', 'r')

def check(x, y):
    if x < 0 or x >= N or y < 0 or y >= N: return False
    if arr[x][y] == 0: return False
    return True

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    find = 0
    for x in range(N):
        for y in range(N):
            if check(x, y) and (check(x, y-1) != 1):
                cnt = 0
                for i in range(N - y):
                    if check(x, y+i):
                        cnt += 1
                    else:
                        break
                if cnt == K:
                    find += 1
                cnt = 0
            if check(x,y) and (not check(x-1, y)):
                cnt = 0
                for j in range(N - x):
                    if check(x+j, y):
                        cnt += 1
                    else:
                        break
                if cnt == K:
                    find += 1



    print('#{} {}'.format(tc, find))


