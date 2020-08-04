import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
numbers = list(map(int, input().split()))

total = len(numbers)
numbers.sort()
idx = (total // 2)
median = numbers[idx]

print('{}'.format(median))