import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    colors = int(input())
    points = [0] * colors
    reds = []
    blues = []
    purple = []

    for color in range(colors):
        points[color] = list(map(int, input().split()))

        if points[color][4] == 1:
            for rx in range(points[color][0], points[color][2] + 1):
                for ry in range(points[color][1], points[color][3] + 1):
                    reds += [(rx, ry)]

        if points[color][4] == 2:
            for bx in range(points[color][0], points[color][2] + 1):
                for by in range(points[color][1], points[color][3] + 1):
                    blues += [(bx, by)]

        count = 0
        for red in reds:
            if red in blues:
                count += 1


    print('#{} {}'.format(t, count))


