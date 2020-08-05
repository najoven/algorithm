import sys
sys.stdin = open("input.txt", 'r')

T = 10
N = 100
M = 100
arr = [0 for _ in range(100)]



for t in range(1, T+1):
    test_case = int(input())
    for i in range(100):
        arr[i] = list(map(int, input().split()))

    addx = 0
    addy = 0

    largest = 0
    for x in range(N):
        addx = 0
        for y in range(M):
            addx += arr[x][y]
            if largest <= addx:
                largest = addx
    for y in range(M):
        addy = 0
        for x in range(N):
            addy += arr[x][y]
            if largest <= addy:
                largest = addy

    diagplus = 0
    diagminus = 0
    for i in range(N):
        diagplus += arr[i][i]
        diagminus += arr[i][100-i-1]
        i += 1

    if largest <= diagplus:
        largest = diagplus
    if largest <= diagminus:
        largest = diagminus

    print('#{} {}'.format(t, largest))







