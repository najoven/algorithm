import sys; sys.stdin = open('input.txt', 'r')

def inorder(v):
    if v == 0: return
    inorder(L[v])
    print(C[v], end='')
    inorder(R[v])


for tc in range(1, 11):
    V = int(input())

    L = [0] * (V + 1)
    R = [0] * (V + 1)
    C = [0] * (V + 1)

    for i in range(V):
        inlist = list(map(str, input().split()))

        if len(inlist) == 4:
            C[int(inlist[0])] = inlist[1]
            L[int(inlist[0])] = int(inlist[2])
            R[int(inlist[0])] = int(inlist[3])
        elif len(inlist) == 3:
            C[int(inlist[0])] = inlist[1]
            L[int(inlist[0])] = int(inlist[2])
        else:
            C[int(inlist[0])] = (inlist[1])


    print('#{} '.format(tc), end='')
    inorder(1)
    print()