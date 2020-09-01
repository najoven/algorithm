import sys; sys.stdin = open('input.txt', 'r')

scores = [list(map(int, input().split())) for _ in range(5)]

best = 0
for x in range(5):
    total = 0
    for y in range(4):
        total += scores[x][y]
    if total > best:
        best = total
        winner = x + 1

print(winner, best)

