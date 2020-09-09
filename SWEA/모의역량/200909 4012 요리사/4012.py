import sys; sys.stdin = open('sample_input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    arr = []
    for i in range(N):
        arr += [i]

    diff = []
    ans = 0xfffffff
    def subset(k):  # k번 요소, 함수 호출의 깊이
        if k == N:
            if len(A) == len(B):
                sumA = 0
                sumB = 0
                for i in range(0, N//2):
                    for j in range(0, N//2):
                        sumA += S[A[i]][A[j]]
                        sumB += S[B[i]][B[j]]
                global ans; ans = min(ans, abs(sumA-sumB))
        else:
            A.append(arr[k])
            subset(k + 1)  # k번 요소를 A에 포함하는 선택
            A.pop()

            B.append(arr[k])
            subset(k + 1)  # k번 요소를 B에 포함하는 선택
            B.pop()


    A, B = [arr[0]], []
    subset(1)
    print('#{} {}'.format(tc, ans))
