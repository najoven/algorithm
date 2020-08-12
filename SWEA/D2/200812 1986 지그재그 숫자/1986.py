import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())

    result = 0
    for num in range(1, N+1):
        if num % 2:
            result += num
        else:
            result -= num

    print('#{} {}'.format(t, result))