import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    cost_A = W * P

    if W > R:
        cost_B = (Q + ((W-R) * S))
    else:
        cost_B = Q

    if cost_A >= cost_B:
        cost = cost_B
    else:
        cost = cost_A

    print('#{} {}'.format(t, cost))
