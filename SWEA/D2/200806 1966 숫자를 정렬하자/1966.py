import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = ''
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            min_idx = i
            if numbers[i] > numbers[j]:
                min_idx = j
            numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    for number in numbers:
        result += ' ' + str(number)

    print('#{}{}'.format(t, result))