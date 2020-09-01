import sys; sys.stdin=open('sample_input.txt', 'r')

def rsp(i, j):
    x = cards[i-1]
    y = cards[j-1]
    if {x, y} == {1, 2}:
        if x == 2:
            return i
        else:
            return j
    elif {x, y} == {2, 3}:
        if x == 3:
            return i
        else: return j
    elif {x, y} == {1, 3}:
        if x == 1:
            return i
        else: return j
    elif x == y:
        return i

def winner(start, end):
    if start == end:
        return start
    start1 = winner(start, (start+end)//2)
    start2 = winner((start+end)//2 + 1, end)
    return rsp(start1, start2)

for tc in range(1, int(input())+1):
    N = int(input())
    cards = list(map(int, input().split()))

    result = []

    print('#{} {}'.format(tc, winner(1, N)))
