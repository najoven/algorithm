import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    test = numbers[0]
    for number in numbers:
        if number > test:
            test = number
    print('#{} {}'.format(t, test))