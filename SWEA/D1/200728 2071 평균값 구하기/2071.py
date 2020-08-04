import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    add_all = 0
    for number in numbers:
        add_all += number
    average_all = round(add_all / len(numbers))
    print('#{} {}'.format(t, average_all))