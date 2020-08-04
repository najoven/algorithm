import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    date = str(input())

    year = date[0] + date[1] + date[2] + date[3]
    month = date[4] + date[5]
    day = date[6] + date[7]

    if (int(month) < 1) or (int(month) > 12):
        print('#{} -1'.format(t))
    else:
        if int(month) == (1 or 3 or 5 or 7 or 8 or 10 or 12):
            if (int(day) < 0) or (int(day) > 31):
                print('#{} -1'.format(t))
            else:
                print('#{} {}/{}/{}'.format(t, year, month, day))
        elif int(month) == 2:
            if (int(day) < 0) or (int(day) > 28):
                print('#{} -1'.format(t))
            else:
                print('#{} {}/{}/{}'.format(t, year, month, day))
        else:
            if (int(day) < 0) or (int(day) > 30):
                print('#{} -1'.format(t))
            else:
                print('#{} {}/{}/{}'.format(t, year, month, day))