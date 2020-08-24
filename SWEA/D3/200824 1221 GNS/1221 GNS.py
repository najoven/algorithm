import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    num, cases = map(str, input().split())

    numbers_list = list(input().split())
    names = {'ZRO': 0, 'ONE' : 0, 'TWO' : 0, 'THR' : 0, 'FOR' : 0, 'FIV' : 0, 'SIX' : 0, 'SVN' : 0, 'EGT' : 0, 'NIN' : 0 }

    for number in numbers_list:
        names[number] += 1

    print(num)
    for name in names:
        print((name + ' ') * names[name], end='')

