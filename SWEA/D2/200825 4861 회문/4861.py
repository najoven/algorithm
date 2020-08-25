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
                    return ''.join(check)
            else:
                til = M//2
                check1 = check[:til]
                check2 = check[-1:til-1:-1]
                if check1 == check2:
                    return ''.join(check)

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
                    return ''.join(check)
            else:
                til = M//2
                check1 = check[:til]
                check2 = check[-1:til-1:-1]
                if check1 == check2:
                    return ''.join(check)



T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    case = []
    for _ in range(N):
        case += [list(list(i for i in input()))]
    result = find(N,M,case)


    print('#{} {}'.format(t, result))




