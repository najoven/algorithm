import sys
sys.stdin = open('input.txt', 'r')

def find(N,M,case):
    for i in range(N):
        for j in range(N - M + 1):
            check = case[i][j:j+M]
            if M % 2 :
                til = M//2
                check1 = check[:til]
                check2 = check[-1:til:-1]
                if check1 == check2:
                    return len(check)
            else:
                til = M//2
                check1 = check[:til]
                check2 = check[-1:til-1:-1]
                if check1 == check2:
                    return len(check)

    for j in range(N):
        for i in range(N-M+1):
            check = []
            for k in range(M):
                check += [case[i+k][j]]
            if M % 2 :
                til = M//2
                check1 = check[:til]
                check2 = check[-1:til:-1]
                if check1 == check2:
                    return len(check)
            else:
                til = M//2
                check1 = check[:til]
                check2 = check[-1:til-1:-1]
                if check1 == check2:
                    return len(check)
    return 1

T = 10
N = 100

for t in range(1, T+1):
    case = int(input())

    pel = []
    for _ in range(N):
        pel += [list(list(i for i in input()))]

    count = 1
    for M in range(N+1):
        length = find(N,M,pel)
        if count <= length:
            count = length

    print('#{} {}'.format(t, count))

