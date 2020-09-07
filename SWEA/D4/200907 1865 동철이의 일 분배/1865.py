import sys; sys.stdin = open('input.txt', 'r')


def perm(n, k, curmul):
    global ans
    if ans >= curmul: return
    if k == n:
        ans = max(ans, curmul)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1, curmul * perc[k][arr[k]])
            arr[k], arr[i] = arr[i], arr[k]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [i for i in range(0, N)]
    perc = [list(map(lambda a: a*0.01, map(int, input().split()))) for _ in range(N)]
    ans = - N * 1
    perm(N, 0, 1)
    ans = ans*100
    print('#{} {:.6f}'.format(tc, ans))