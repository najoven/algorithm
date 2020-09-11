import sys; sys.stdin = open('sample_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    scores= []
    visit = [[0] * (sum(arr) + 1) for _ in range(N + 1)]

    def subset(k, cur_sum):
        if visit[k][cur_sum]: return
        visit[k][cur_sum] = 1
        if k == N:
            scores.append(cur_sum)
            return
        else:
            subset(k + 1, cur_sum + arr[k])
            subset(k + 1, cur_sum)

    subset(0, 0)
    print('#{} {}'.format(tc, len(scores)))