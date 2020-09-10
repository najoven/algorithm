import sys; sys.stdin = open('sample_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())

    numbers = [i for i in range(1, N+1)]

    L = [0] * (N + 1)
    R = [0] * (N + 1)

    for i in range(1, N+1):
        if i * 2 <= N:
            L[i] = i * 2
            if i * 2 + 1 <= N:
                R[i] = i * 2 + 1

    result = [i for i in range(0, N+1)]
    def inorder(v):
        if v == 0: return
        inorder(L[v])
        result[v] = numbers.pop(0)
        inorder(R[v])

    inorder(1)
    print('#{} {} {}'.format(tc, result[1], result[N//2]))
