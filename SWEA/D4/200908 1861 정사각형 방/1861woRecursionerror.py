import sys; sys.stdin = open('input.txt', 'r')


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    arr_list = [0] * (N**2)
    cnt_list = [0] * (N**2)
    for x in range(N):
        for y in range(N):
            a = arr[x][y]
            cnt = 1
            while 1:
                for l in range(4):
                    tx = x + dx[l]
                    ty = y + dy[l]
                    if tx < 0 or tx >= N or ty < 0 or ty >= N: continue
                    if arr[tx][ty] - arr[x][y] == 1:
                        x = tx
                        y = ty
                        cnt += 1
                        break
                else:
                    break
            arr_list[a-1] = cnt


    ans = 0
    coor = 0
    for i in range(len(arr_list)):
        cnt = arr_list[i]
        if cnt > ans:
            ans = cnt
            coor = i

    print('#{} {} {}'.format(tc, coor+1, ans))

