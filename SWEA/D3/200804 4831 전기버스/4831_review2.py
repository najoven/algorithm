import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

for t in range(1, T+1):
    K, N, M = (map(int, input().split()))

    station = [0] + list(map(int, input().split())) +[N]

    bus = 0
    ans = 0
    for i in range(1, M + 1 + 1):
        if station[i - 1] + K < station[i]:
            ans = 0
            break
        if bus + K < station[i]:
            bus = station[i - 1]
            ans += 1
    print('#{} {}'.format(t, ans))