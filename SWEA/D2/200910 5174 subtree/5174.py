import sys; sys.stdin = open('sample_input.txt', 'r')

def treesize(v):
    global cnt
    if v == 0: return 0
    l = treesize(L[v])
    r = treesize(R[v])
    cnt += 1
    return l + r + 1

for tc in range(1, int(input()) + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    L = [0] * (E+2)
    P = [0] * (E+2)
    R = [0] * (E+2)

    for i in range(0, E*2, 2):
        p, c = arr[i], arr[i+1]
        if not L[p]:
            L[p] = c
        else: R[p] = c

    cnt = 0
    print('#{} {}'.format(tc, treesize(N)))


