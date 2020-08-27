import sys
sys.stdin = open('sample_input.txt', 'r')

def paper(N):
        if N == 1:
            return 1
        elif N == 2:
            return 3
        else:
            result = paper(N-1) + 2 * paper(N-2)
            return result

T = int(input())
for t in range(1, T+1):
    N = int(input())
    N = N // 10
    result = paper(N)

    if not N % 2:
        result = result - (2 * (N // 2 - 1))

    print('#{} {}'.format(t, result))