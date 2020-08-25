import sys
sys.stdin = open('input.txt', 'r')


cases = int(input())
for case in range(1, cases+1):
    P = input()
    T = input()
    if P in T:
        result = 1
    else:
        result = 0
    print('#{} {}'.format(case, result))

