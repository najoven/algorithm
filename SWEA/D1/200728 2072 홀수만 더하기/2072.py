import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    result = 0
    for number in numbers:
        if number % 2:
            result += number
    print('#{} {}'.format(t, result))