import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for t in range(1, T + 1):
    knm = list(map(int, input().split()))
    bus_stops = list(map(int, input().split()))

    travel = knm[0]
    arrive = knm[1]
    travel_list = list(range(0, knm[1]+1))

    distance_traveled = 0
    count = 0


    for i in range(1, len(bus_stops)+1):
        if distance_traveled + travel >= arrive:
            break
        if i != len(bus_stops) and bus_stops[i] - bus_stops[i-1] > travel:
            count = 0
            break

        for j in range(len(bus_stops) -1, -1, -1):

            if bus_stops[j] <= distance_traveled + travel:
                distance_traveled = bus_stops[j]
                count += 1
                break

    print('#{} {}'.format(t, count))

