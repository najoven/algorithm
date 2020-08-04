import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for t in range(1,T+1):
    nm = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    sum_list = []
    for i in range(nm[1] - 1, len(numbers)):
        sum = 0

        for d in range((i-nm[1]+1), i+1):
            sum += numbers[d]
        sum_list += [sum]


    min_num = sum_list[0]
    max_num = sum_list[0]
    for k in sum_list:
        if min_num >= k:
            min_num = k
        if max_num <= k:
            max_num = k

    difference = max_num - min_num

    print('#{} {}'.format(t, difference))
