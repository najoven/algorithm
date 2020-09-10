import sys; sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())

    P = [0] * (N + 1)
    T = [0] * (N + 1)
    for _ in range(N):
        arr = list(map(str, input().split()))
        if len(arr) == 4:
            T[int(arr[0])] = arr[1]
            P[int(arr[2])] = int(arr[0])
            P[int(arr[3])] = int(arr[0])
        if len(arr) == 2:
            T[int(arr[0])] = int(arr[1])



    for c in range(N, 0, -2):
        p = P[c]
        if T[p] == '-':
            T[p] = T[c-1] - T[c]
        elif T[p] == '+':
            T[p] = T[c-1] + T[c]
        elif T[p] == '*':
            T[p] = T[c-1] * T[c]
        elif T[p] == '/':
            T[p] = T[c-1] / T[c]

    print('#{} {}'.format(tc, int(T[1])))
