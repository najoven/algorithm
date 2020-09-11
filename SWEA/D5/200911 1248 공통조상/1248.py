import sys; sys.stdin = open('input.txt', 'r')

def treesize(v):
    global cnt
    if v == 0: return 0
    l = treesize(L[v])
    r = treesize(R[v])
    cnt += 1
    return l + r + cnt

for tc in range(1, int(input())+1):
    V, E, x, y = map(int, input().split())
    arr = list(map(int, input().split()))

    L = [0] * (V + 1)
    R = [0] * (V + 1)
    P = [0] * (V + 1)

    for i in range(0, E*2, 2):
        P[arr[i+1]] = arr[i]
        if L[arr[i]] == 0:
            L[arr[i]] = arr[i+1]
        else:
            R[arr[i]] = arr[i+1]


    resultx = []
    while P[x] != 0:
        resultx.append(P[x])
        x = P[x]

    resulty = []
    while P[y] != 0:
        resulty.append(P[y])
        y = P[y]

    if len(resultx) < len(resulty):
        for r in resultx:
            if r in resulty:
                coor = r
                break
    else:
        for r in resulty:
            if r in resultx:
                coor = r
                break

    cnt = 0
    treesize(coor)

    print('#{} {} {}'.format(tc, coor, cnt))