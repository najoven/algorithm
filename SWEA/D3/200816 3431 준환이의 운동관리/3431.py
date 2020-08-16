import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    L, U, X = map(int, input().split())

    if X > U:
        result = -1
    elif X < U:
        if X >= L:
            result = 0
        else:
            result = L - X

    print('#{} {}'.format(t, result))