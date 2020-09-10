import sys; sys.stdin = open('sample_input.txt', 'r')

def push(item):
    H.append(item)
    N = len(H)
    c = N-1
    p = c // 2

    while H[p]:
        if H[p] and H[c] < H[p]:
            H[p], H[c] = H[c], H[p]
            c = p
            p = c // 2
        else: break

for tc in range(1, int(input())+1):
    V = int(input())
    arr = list(map(int, input().split()))
    H = [0]
    hsize = 0
    for i in arr:
        push(i)

    lastv = len(H) - 1
    result = H[0]
    p = lastv // 2
    while p:
        result += H[p]
        p = p // 2

    print('#{} {}'.format(tc, result))

