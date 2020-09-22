import sys; sys.stdin = open('input.txt', 'r')

smalls = []
for _ in range(9):
    smalls += [int(input())]

more = sum(smalls) - 100

signal = 0
for i in range(9):
    for j in range(9):
        if i != j and smalls[i] + smalls[j] == more:
            smalls[i] = 100
            smalls[j] = 100
            signal = 1
            break
    if signal == 1:
        break

for i in range(8):
    for j in range(i+1, 9):
        if smalls[i] > smalls[j]:
            smalls[i], smalls[j] = smalls[j], smalls[i]

for i in range(7):
    print(smalls[i])