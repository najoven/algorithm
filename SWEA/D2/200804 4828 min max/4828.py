import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for t in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    
    min_num = numbers[0]
    max_num = numbers[0]
    for number in numbers:
        if min_num >= number:
            min_num = number
        if max_num <= number:
            max_num = number

    difference = max_num - min_num
    print('#{} {}'.format(t, difference))