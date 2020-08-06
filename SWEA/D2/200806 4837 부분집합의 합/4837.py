import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
A = list(range(1, 13))
M = len(A)
for t in range(1, T+1):
    N, K = map(int, input().split())

    N_combs = []
    for i in range(1<<M):
        S = 0
        combs = []

        for j in range(M):
            if i & (1<<j):
                combs += [A[j]]
        N_combs += [combs]

        count = 0
        for N_comb in N_combs:
            S = 0
            if len(N_comb) == N:
                for n in N_comb:
                    S += n
                if S == K:
                    count += 1

    print('#{} {}'.format(t, count))

