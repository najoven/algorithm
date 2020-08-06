import sys
sys.stdin('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    days = int(input())
    income_list = list(map(int, input().split()))

    add = 0
    start = 0

    max_income = income_list[-1]
    for i in range(len(income_list) - 2, -1, -1):
        if max_income > income_list[i]:
            add += (max_income - income_list[i])
        elif max_income < income_list[i]:
            max_income = income_list[i]

    print('#{} {}'.format(t, add))

