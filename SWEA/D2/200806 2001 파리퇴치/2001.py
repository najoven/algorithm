import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    flies_list = []
    for i in range(0, N):
        flies_sublist = list(map(int, input().split()))
        flies_list.append(flies_sublist)

    result = 0
    for x in range(0, N-M+1):
        for y in range(0, N-M+1):
            fly_sum = 0
            for i in range(0, M):
                for j in range(0, M):
                    fly_sum += flies_list[x + i][y + j]

            if fly_sum > result:
                result = fly_sum

    print('#{} {}'.format(t, result))