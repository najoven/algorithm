import sys
sys.stdin = open('sample_input.txt', 'r')

def check(arr):
    for i in range(len(arr)):
        if arr[i] == '(':   # push
            stack.append(arr[i])
        elif arr[i] == ')': # pop하고 비교
            if len(stack) == 0:
                return 0
            else:
                a = stack.pop()
                if a != '(':
                    return 0

        if arr[i] == '{':   # push
            stack.append(arr[i])
        elif arr[i] == '}': # pop하고 비교
            if len(stack) == 0:
                return 0
            else:
                a = stack.pop()
                if a != '{':
                    return 0

    if stack: return 0
    else: return 1

T = int(input())

for t in range(1, T+1):
    stack = []
    arr = input()
    print('#{} {}'.format(t, check(arr)))