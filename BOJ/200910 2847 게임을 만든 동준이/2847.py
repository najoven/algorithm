import sys; sys.stdin = open('input.txt', 'r')

N = int(input())

arr = []
for _ in range(N):
    arr += [int(input())]

result = 0
for i in range(N-2, -1, -1):
    if arr[i+1] < arr[i]:
        result += arr[i] - (arr[i+1] - 1)
        arr[i] = arr[i+1] - 1
    elif arr[i+1] == arr[i]:
        result += 1
        arr[i] = arr[i+1] - 1

print(result)