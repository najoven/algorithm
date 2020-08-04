import sys
sys.stdin = open('input.txt', 'r')

T = list(map(int, input().split()))
P = T[0]
K = T[1]

count = 0
while K <= P:
    count += 1
    K += 1

print(count)