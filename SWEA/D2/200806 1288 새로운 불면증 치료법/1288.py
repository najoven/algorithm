import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    numbers = input()
    check_num = [0] * 10

    sum_num = 0
    count = 0
    int_number = int(numbers)
    origin = int(numbers)
    while sum_num < 10:
        for number in numbers:
            if check_num[int(number)] == 0:
                check_num[int(number)] += 1
                sum_num += 1
        int_number += origin
        numbers = str(int_number)
        count += 1
    print('#{} {}'.format(t, count * origin))