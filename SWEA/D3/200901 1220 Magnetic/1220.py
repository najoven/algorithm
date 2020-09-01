import sys; sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    T = int(input())
    magnets = [list(map(int, input().split())) for _ in range(T)]

    #N: 1, S:2
    cnt = 0
    for y in range(T):
        visit = 0
        for x in range(T):
            if magnets[x][y] == 1:
                visit = 1
            elif visit == 1 and magnets[x][y] == 2:
                magnets[x][y] = 0
                cnt += 1
                visit = 0

    print('#{} {}'.format(tc, cnt))