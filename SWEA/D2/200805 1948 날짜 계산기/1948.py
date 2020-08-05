import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
month_31 = [1, 3, 5, 7, 8, 10, 12]

for t in range(1, T+1):
    date_list = list(map(int, input().split()))
    result = 0
    remain = 0
    if date_list[0] == date_list[2]:
        result = date_list[3] - date_list[1] + 1
    else:
        if date_list[0] in month_31:
            remain = 31
        elif date_list[0] == 2:
            remain= 28
        else:
            remain = 30

        for month in range(date_list[0] + 1, date_list[2]):
            if month in month_31:
                result += 31
            elif month == 2:
                result += 28
            else:
                result += 30

        result += (remain - date_list[1] + 1) + date_list[3]

    print('#{} {}'.format(t, result))
