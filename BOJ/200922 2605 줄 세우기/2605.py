import sys; sys.stdin = open('input.txt', 'r')

N = int(input())
cards = list(map(int, input().split()))
places = [0] * N
for i in range(N):
    if cards[i] == 0:
        places[i] = i+1
    else:
        places.insert(i - cards[i], i+1)

for i in places:
    if i != 0:
        print(i, end=' ')
