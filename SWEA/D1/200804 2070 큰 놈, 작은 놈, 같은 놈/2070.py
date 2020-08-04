import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    comparison = numbers[0]
    if comparison < numbers[1]:
        print('#{} <'.format(t))
    elif comparison == numbers[1]:
        print('#{} ='.format(t))
    else:
        print('#{} >'.format(t))