import sys
sys.stdin = open('input.txt', 'r')
import copy

def ladderfind(ladders, y):
    dx = [0, 0, 1]
    dy = [-1, 1, 0]
    ladders1 = copy.deepcopy(ladders)
    x = 0
    cnt = 0
    while x <= 99:
        for i in range(3):
            testx = x + dx[i]
            testy = y + dy[i]
            if cnt == 0:
                initesty = testy
            if testx == 99:
                return cnt, initesty
            if 0 <= testy < N and 0 <= testx < N and ladders1[testx][testy] != 0:
                x = testx
                y = testy
                ladders1[testx][testy] = 0
                cnt += 1
                break



T = 10
N = 100

for t in range(1, T+1):
    case = int(input())
    ladders = [list(map(int, input().split())) for _ in range(N)]
    cnts = []
    ys = []

    for y in range(N):
        if ladders[0][y] != 0:
            cnt, testy = ladderfind(ladders,y)
            cnts += [cnt]
            ys += [testy]

    min_cnt = min(cnts)
    result = 0
    for i in range(len(cnts)):
        if cnts[i] == min_cnt:
            testy = ys[i]
            if testy >= result:
                result = testy
    print('#{} {}'.format(t, result))