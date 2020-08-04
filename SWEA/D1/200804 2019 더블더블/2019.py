import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
result = 1
print(result, end=' ')
for i in range(0, T):
    result *= 2
    print(result, end=' ')