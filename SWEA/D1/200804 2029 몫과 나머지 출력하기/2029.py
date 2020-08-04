import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    divide = list(map(int, input().split()))
    quot = divide[0] // divide[1]
    remaind = divide[0] % divide[1]

    print('#{} {} {}'.format(t, quot, remaind))