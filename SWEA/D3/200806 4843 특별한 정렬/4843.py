import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(len(numbers) - 1):
        if not i % 2:
            max = i
            for j in range(i+1, len(numbers)):
                if numbers[max] < numbers[j]:
                    max = j
            numbers[i], numbers[max] = numbers[max], numbers[i]
            # print(numbers)
        elif i % 2:
            min = i
            for j in range(i+1, len(numbers)):
                if numbers[min] > numbers[j]:
                    min = j
            numbers[i], numbers[min] = numbers[min], numbers[i]
            # print(numbers)

    number_str = ''
    for idx in range(0, 10):
        number_str += ' ' + str(numbers[idx])

    print('#{}{}'.format(t, number_str))