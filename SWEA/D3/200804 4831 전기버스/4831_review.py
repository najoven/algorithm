import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

for t in range(1, T+1):
    K, N, M = (map(int, input().split()))
    numbers = list(map(int, input().split()))
    station = [0] * (N + 1)
    for val in numbers:
        station[val] = 1

    bus = 0
    ans = 0
    while bus + K < N:
        prev = bus
        for i in range(bus + K, bus, -1):
            if station[i]:
                bus = i
                ans += 1
                break
        if bus == prev:
            ans = 0; break
    print('# {} {}'.format(t, ans))
