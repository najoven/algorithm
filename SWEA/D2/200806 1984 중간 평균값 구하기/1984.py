import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    sum_total = 0
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            min = i
            if numbers[i] > numbers[j]:
                min = j
            numbers[i], numbers[min] = numbers[min], numbers[i]

        if i != 0:
            sum_total += numbers[i]
    average_total = round(sum_total / (len(numbers)-2))
    print('#{} {}'.format(t, average_total))


