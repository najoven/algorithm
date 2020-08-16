import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, B = map(int, input().split())
    H_list = list(map(int, input().split()))

    H_combs = []
    for i in range(1<<N):
        H_comb = 0
        for j in range(N):
            if i & (1<<j):
                H_comb += H_list[j]
        if H_comb >= B:
            H_combs += [H_comb]

    # for i in range(len(H_combs)-1, 0, -1):
    #     for j in range(0, i):
    #         if H_combs[j] > H_combs[j+1]:
    #             H_combs[j], H_combs[j+1] = H_combs[j+1], H_combs[j]
    #
    # differences = H_combs[0] - B

    differences = min(H_combs)
    print('#{} {}'.format(t, differences))

