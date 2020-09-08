import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    flag_list = []
    flag_list = [list(input()) for _ in range(N)]
    min_count = N * M
    arr = range(N)

    count_list = []
    for i in range(N):
        count_list.append([flag_list[i].count('W'), flag_list[i].count('B'), flag_list[i].count('R')])

    for i in range(0, N - 3 + 1):
        for j in range(i + 1, N - 2 + 1):
            count = 0
            for x in arr[: i+1]:
                count += count_list[x][1] + count_list[x][2]
            for y in arr[i+1:j+1]:
                count += count_list[y][0] + count_list[y][2]
            for z in arr[j+1:]:
                count += count_list[z][0] + count_list[z][1]
            if count <= min_count:
                min_count = count

    print('#{} {}'.format(t, min_count))

