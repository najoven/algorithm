import sys; sys.stdin = open('sample_input.txt', 'r')

def check(x, y):
    if x < 0 or x >= N or y < 0 or y >= N: return False
    return True


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    play = [[0] * N for _ in range(N)]

    already = N // 2
    play[already][already] = 2
    play[already-1][already] = 1
    play[already][already-1] = 1
    play[already-1][already-1] = 2


    dx = [0, 0, -2, -2, 2, 2, -2, 2]
    dy = [-2, 2, -2, 2, -2, 2, 0, 0]
    cx = [0, 0, -1, -1, 1, 1, -1, 1]
    cy = [-1, 1, -1, 1, -1, 1, 0, 0]
    diffs = len(dx)
    opposite = {1:2, 2:1}

    for _ in range(M):
        x, y, c = map(int, input().split())
        x, y = y-1, x-1

        for l in range(diffs):
            if (check(x+dx[l], y+dy[l])) and (play[x+cx[l]][y+cy[l]] == opposite[c]):
                ilist = []
                jlist = []
                i = x
                j = y
                for _ in range(N):
                    if check(i+cx[l],j+cy[l]) and play[i+cx[l]][j+cy[l]] == c:
                        break
                    elif (check(i+cx[l],j+cy[l]) and play[i+cx[l]][j+cy[l]] == 0) or _ == N-1:
                        ilist = []
                        jlist = []
                        break
                    elif check(i, j) and check(i+cx[l], j+cy[l]) and play[i+cx[l]][j+cy[l]] == opposite[c]:
                        i += cx[l]
                        j += cy[l]
                        ilist += [i]
                        jlist += [j]

                if ilist:
                    for q in range(len(ilist)):
                        if check(ilist[q],jlist[q]):
                            play[x][y] = c
                            play[ilist[q]][jlist[q]] = c

    count1 = 0
    count2 = 0
    for _ in range(N):
        count1 += play[_].count(1)
        count2 += play[_].count(2)
    print('#{} {} {}'.format(tc, count1, count2))