import sys; sys.stdin = open('sample_input.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))

    Qpizzas = []
    for i in range(M):
        Qpizzas.append([i, pizzas[i]])

    Q = []
    for i in range(N):
        Q.append(Qpizzas.pop(0))

    while len(Q) > 1:
        front = Q[0][1] // 2
        if front == 0:
            Q.pop(0)
            if Qpizzas:
                Q.append(Qpizzas.pop(0))
        else:
            Q[0][1] = front
            Q.append(Q.pop(0))

    print('#{} {}'.format(tc, Q[0][0]+1))

