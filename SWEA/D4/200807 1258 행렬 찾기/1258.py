import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):

    N = int(input())
    arr = []
    for _ in range(0, N):
        arr += [list(map(int, input().split()))]

    area_list = []
    last_coor_list = []

    startx = 0
    starty = 0
    for i in range(startx, N):
        for j in range(starty, N):
            x = 0
            y = 0
            h = 0
            b = 0
            if arr[i][j]:
                for dx in range(0, N-i):
                    if dx != N-i-1:
                        if arr[i+dx+1][j] == 0:
                            dx += 1
                            break
                    elif dx == N-i-1:
                        dx = N-i
                        break

                for dy in range(0, N-j):
                    if dy != N-j-1:
                        if arr[i][j+dy+1] == 0:
                            dy += 1
                            break
                    elif dy == N-j-1:
                        dy = N-j
                        break

                x = i + dx - 1
                y = j + dy - 1


                # print('종점제발 {} {} {} {}'.format(x, y, dx, dy))

                if (x,y) not in last_coor_list:
                    last_coor_list += [(x,y)]
                    area_list += [[dx, dy, dx*dy]]


    for i in range(len(area_list)-1, 0, -1):
        for j in range(0, i):
            if area_list[j][2] > area_list[j+1][2]:
                area_list[j][0], area_list[j+1][0] = area_list[j+1][0], area_list[j][0]
                area_list[j][1], area_list[j + 1][1] = area_list[j + 1][1], area_list[j][1]
                area_list[j][2], area_list[j + 1][2] = area_list[j + 1][2], area_list[j][2]
            if area_list[j][2] == area_list[j+1][2]:
                if area_list[j][0] > area_list[j+1][0]:
                    area_list[j][0], area_list[j + 1][0] = area_list[j + 1][0], area_list[j][0]
                    area_list[j][1], area_list[j + 1][1] = area_list[j + 1][1], area_list[j][1]
                    area_list[j][2], area_list[j + 1][2] = area_list[j + 1][2], area_list[j][2]


    result = ''
    for area in area_list:
        for i in range(0,2):
            result += ' ' + str(area[i])
    count = len(area_list)
    print('#{} {}{}'.format(t, count, result))