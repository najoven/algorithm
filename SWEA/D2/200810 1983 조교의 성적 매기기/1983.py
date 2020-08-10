import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())

    total = [0] * N

    for student in range(1, N+1):
        scores = list(map(int, input().split()))
        total[student-1] = [((0.35 * scores[0]) + (0.45 * scores[1]) + (0.2 * scores[2])), student]


    for i in range(0, len(total) - 1):
        for j in range(i + 1, len(total)):
            max_idx = i
            if total[max_idx][0] < total[j][0]:
                max_idx = j
            total[i], total[max_idx] = total[max_idx], total[i]

    rank_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    for k in range(len(total)):
        if total[k][1] == K:
            rank = int(k // (N / 10))
            print('#{} {}'.format(t, rank_list[rank]))


