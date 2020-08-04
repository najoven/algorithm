import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

total = 0
while T > 10:
    total += T % 10
    T = T // 10
total += T

print('{}'.format(total))