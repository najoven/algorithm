import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    cases = int(input())
    print('#{}'.format(t))
    count = 0
    for case in range(cases):
        letter, numbers = map(str, input().split())
        numbers = int(numbers)
        for number in range(numbers):
            print('{}'.format(letter), end='')
            count += 1
            if count == 10:
                print()
                count = 0
    print()