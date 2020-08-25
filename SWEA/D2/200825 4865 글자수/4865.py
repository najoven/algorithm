import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    str1 = list(i for i in input())
    str2 = list(i for i in input())
    max_count = 0

    for i in str1:
        count = 0
        for j in str2:
            if i == j:
                count += 1
        if count >= max_count:
            max_count = count

    print('#{} {}'.format(t, max_count))