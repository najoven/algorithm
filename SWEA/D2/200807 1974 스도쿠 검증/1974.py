import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    arr = []
    for _ in range(9):
        arr += [list(map(int, input().split()))]

    result = 1

    for i in range(9):
        add = 0
        for j in range(0, 9):
            add += arr[i][j]
        if add != 45:
            result = 0
            break

    for i in range(9):
        add = 0
        for j in range(0, 9):
            add += arr[j][i]
        if add != 45:
            result = 0
            break


    dx = 0
    dy = 0
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            add = 0
            for dx in range(3):
                for dy in range(3):
                    add += arr[i + dx][i + dy]

            if add != 45:
                result = 0
                break



    print('#{} {}'.format(t, result))