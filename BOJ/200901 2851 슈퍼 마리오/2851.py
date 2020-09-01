import sys; sys.stdin = open('input.txt', 'r')

mushrooms = []
for _ in range(10):
    mushrooms += [int(input())]

total = 0
min = 100
for i in range(10):
    total += mushrooms[i]
    if abs(100-total) <= min:
        min = abs(100-total)
        result = total

print(result)

