import sys
sys.stdin = open("input.txt", 'r')

T = 10
for t in range(1, T+1):
    cases = int(input())
    yellows = list(map(int, input().split()))


    for case in range(0, cases):
        max_count = 0
        min_count = 0

        min_yellows = yellows[0]
        max_yellows = yellows[0]
        for yellow in yellows:
            if min_yellows >= yellow:
                min_yellows = yellow
            if max_yellows <= yellow:
                max_yellows = yellow


        for i in range(0, len(yellows)):
            if yellows[i] == max_yellows and (max_count == 0):
                yellows[i] = (max_yellows - 1)
                max_count += 1
            if yellows[i] == min_yellows and (min_count == 0):
                yellows[i] = (min_yellows + 1)
                min_count += 1

    print('#{} {}'.format(t, (max(yellows) - min(yellows))))