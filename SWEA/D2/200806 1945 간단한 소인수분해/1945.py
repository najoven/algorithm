import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    number = int(input())
    div_list = [0, 0, 0, 0, 0]


    zero = 0
    divn_list = [2, 3, 5, 7, 11]
    while number > 1:
        for i in range(0, 5):
            if not number % divn_list[i]:
                div_list[i] += 1
                number /= divn_list[i]
    a = div_list[0]
    b = div_list[1]
    c = div_list[2]
    d = div_list[3]
    e = div_list[4]

    print('#{} {} {} {} {} {}'.format(t, a, b, c, d, e))

