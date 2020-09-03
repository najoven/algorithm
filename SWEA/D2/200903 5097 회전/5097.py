import sys; sys.stdin = open('sample_input.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    print('#{} {}'.format(tc, arr[M % N]))