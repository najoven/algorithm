import sys; sys.stdin = open('input.txt', 'r')

A, B = map(str, input().split())

a = len(A)
b = len(B)

arr = [['.'] * a for _ in range(b)]

set = 0
for i in range(a):
    for j in range(b):
        if A[i] == B[j]:
            set = 1
            break
    if set == 1:
        break

for l in range(a):
    arr[j][l] = A[l]
for l in range(b):
    arr[l][i] = B[l]

blank = ''
for lst in arr:
    print(blank.join(lst))