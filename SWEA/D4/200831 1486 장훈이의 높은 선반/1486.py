import sys
sys.stdin = open('input.txt', 'r')

def heightsets(k, n, cur_sum): # k가 레벨 루트에서 어떤 경로를 따라 왔는지,
    if k == n:
        sumlist.append(cur_sum)
        for i in range(n):
            return
    else:
        bits[k] = 1 # k번 요소에 대한 결정 저장 (k번 요소에 대한 원소를 켜겠다)
        heightsets(k+1, n, cur_sum + heights[k])
        bits[k] = 0 # k번 요소에 대한 결정 저장 (k번 요소에 대한 원소를 끈다)
        heightsets(k+1, n, cur_sum)

for t in range(1, int(input())+1):

    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    bits = [0] * N
    sumlist = []
    heightsets(0, N, 0)

    result = []
    for s in sumlist:
        if s >= B:
            result.append(s-B)

    print('#{} {}'.format(t, min(result)))