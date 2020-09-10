import sys; sys.stdin = open('sample_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    nodetemp = []
    saves = []
    for _ in range(M):
        n, val = map(int, input().split())
        nodetemp.append(n)
        saves.append([n, val])

    R = max(nodetemp)
    tree = [0] * (R + 1)
    for i in saves:
        tree[i[0]] = i[1]

    for c in range(R, 1, -1):
        p = c // 2
        tree[p] += tree[c]

    print('#{} {}'.format(tc, tree[L]))
