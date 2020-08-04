import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    if not T % i:
        print(i, end = ' ')
