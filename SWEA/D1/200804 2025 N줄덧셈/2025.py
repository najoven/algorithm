import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
sum_all = 0
for t in range(T, 0, -1):
    sum_all += t

print(sum_all)