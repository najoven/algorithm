import sys; sys.stdin = open('input.txt', 'r')

symbols = ['/', '*', '+', '-', '(', ')']
def math(calcs):
    for cal in calcs:
        if cal not in symbols:
            final.append(cal)
        else:
            if len(final) >= 2:
                y = int(final.pop())
                x = int(final.pop())
                if cal == '*':
                    final.append(x * y)
                elif cal == '/':
                    final.append(x // y)
                elif cal == '+':
                    final.append(x + y)
                elif cal == '-':
                    final.append(x - y)
    return final[0]


for t in range(1, 11):
    N = int(input())
    calculations = input()
    isp = {'*' : 2, '/' : 2, '+' : 1, '-' : 1, '(' : 0}
    icp = {'*' : 2, '/' : 2, '+' : 1, '-' : 1, '(' : 3}

    S = []
    result = []
    for calculation in calculations:
        if calculation not in symbols:
            result.append(calculation)
        else:
            if not S:
                S.append(calculation)
            elif calculation == ')':
                while S[-1] != '(':
                    result.append(S.pop())
                S.pop()
            elif icp[calculation] >= isp[S[-1]]:
                S.append(calculation)
            elif icp[calculation] < isp[S[-1]]:
                while icp[calculation] < isp[S[-1]]:
                    result.append(S.pop())
                if icp[calculation] >= isp[S[-1]]:
                    S.append(calculation)


    final=[]
    print('#{} {}'.format(t, math(result)))

