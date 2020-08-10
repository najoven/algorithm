import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
for number in range(1, N+1):
    game = ['3', '6', '9']

    count = 0
    for n in str(number):
        if n in game:
            count += 1
    if count == 0:
        print(number, end=' ')
    else:
        print('-'*count, end=' ')

