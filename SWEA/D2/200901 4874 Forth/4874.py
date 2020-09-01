import sys; sys.stdin = open('sample_input.txt', 'r')

def math(calcs):
    error = 'error'
    for cal in calcs:
        if cal not in symbols:
            result.append(cal)
        else:
            if cal == '.':
                if len(result) == 1:
                    return result[0]
                else:
                    return error
            else:
                if len(result) >= 2:
                    y = int(result.pop())
                    x = int(result.pop())
                    if cal == '*':
                        result.append(x * y)
                    elif cal == '/':
                        result.append(x // y)
                    elif cal == '+':
                        result.append(x + y)
                    elif cal == '-':
                        result.append(x - y)
                else:
                    return error

symbols = ['/', '*', '+', '-', '.']
for t in range(1, int(input())+1):
    calcs = list(map(str, input().split()))

    result =[]
    print('#{} {}'.format(t, math(calcs)))
