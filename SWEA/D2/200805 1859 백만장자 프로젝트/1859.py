import sys
sys.stdin('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    countdays = int(input())
    income_list = list(map(int, input().split()))

    addall = 0
    startp = 0
    for i in range(startp, len(income_list)):
        max_income = income_list[startp]
        for k in range(startp, len(income_list)):
            if income_list[k] >= max_income:
                max_income = income_list[k]

        if income_list[i] == max_income:
            for j in range(startp, i):
                addall += (income_list[i] - income_list[j])
            startp = i + 1


    print('#{} {}'.format(t,addall))

