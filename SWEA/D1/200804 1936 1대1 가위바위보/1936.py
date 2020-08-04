import sys
sys.stdin = open('input.txt', 'r')

T = list(map(int, input().split()))

a = T[0]
b = T[1]

if a == 1:
    if b == 3:
        print('A')
    elif b == 2:
        print('B')
elif a == 2:
    if b == 3:
        print('B')
    elif b == 1:
        print('A')
else:
    if b == 1:
        print('B')
    elif b == 2:
        print('A')