import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    flag_list = []
    for _ in range(N):
        flag_list += [list(input())]

    color_patterns = []

    min_count = N * M
    for x in range(1, N-1):
        for y in range(1, N-1):
            for z in range(1, N-1):
                if x + y + z == N:
                    count = 0
                    color_patterns = [x, y, z]
                    for w in range(x):
                        count += M - flag_list[w].count('W')
                    for b in range(x, x+y):
                        count += M - flag_list[b].count('B')
                    for r in range(x+y, x+y+z):
                        count += M - flag_list[r].count('R')
                    if min_count >= count:
                        min_count = count


    print('#{} {}'.format(t, min_count))

