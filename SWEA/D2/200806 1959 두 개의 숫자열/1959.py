import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))

    N = len(N_list)
    M = len(M_list)

    if N <= M:
        max_sum = 0
        for m in range(0, M-N + 1):
            multi = 0
            for n in range(0, N):
                multi += N_list[n] * M_list[m]
                m += 1
            if multi >= max_sum:
                max_sum = multi

    if M <= N:
        max_sum = 0
        for n in range(0, N-M +1):
            multi = 0
            for m in range(0, M):
                multi += N_list[n] * M_list[m]
                n += 1
            if multi >= max_sum:
                max_sum = multi

    print('#{} {}'.format(t, max_sum))




