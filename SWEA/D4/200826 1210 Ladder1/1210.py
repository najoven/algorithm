import sys
sys.stdin = open('input.txt', 'r')

def ladderfind(ladders):
    dx = [0, 0, -1]
    dy = [-1, 1, 0]

    x = 99
    y = ladders[x].index(2)

    while x >= 0:
        for i in range(3):
            testx = x + dx[i]
            testy = y + dy[i]
            if testx == 0:
                return testy
            if 0 <= testy < N and 0 < testx < N-1 and ladders[testx][testy] != 0:
                x = testx
                y = testy
                ladders[testx][testy] = 0
                break




T = 10
N = 100

for t in range(1, T+1):
    case = int(input())
    ladders = [list(map(int, input().split())) for _ in range(N)]

    result = ladderfind(ladders)
    print('#{} {}'.format(case, result))
