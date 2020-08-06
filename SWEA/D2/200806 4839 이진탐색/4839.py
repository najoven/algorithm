import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def bin_search(P, key):
    arr = range(0, P+1)
    start = 1
    end = len(arr) - 1

    count = 0
    while start <= end:
        middle = int((end+start)/2)

        count += 1
        if key == arr[middle]:
            return count
        elif key < arr[middle]:
            end = middle
        elif key > arr[middle]:
            start = middle

for t in range(1, T+1):
    P, A, B = map(int, input().split())
    count_A = bin_search(P, A)
    count_B = bin_search(P, B)

    if count_A < count_B:
        winner = 'A'
    elif count_A > count_B:
        winner = 'B'
    elif count_A == count_B:
        winner = 0

    print('#{} {}'.format(t, winner))






