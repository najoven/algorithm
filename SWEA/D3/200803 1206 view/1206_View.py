import sys
sys.stdin = open("input.txt", "r")
T = 10

for t in range(1,T+1):
    A = []
    count = 0
    case = int(input())
    numbers = list(map(int, input().split()))

    

    max_numb = numbers[0]
    for number in numbers:
        if number >= max_numb:
            max_numb = number


    A = [0] * (len(numbers))


    for i in range(0, len(A)):
        A[i] = [0] * max_numb
        for a in range(0, numbers[i]):
            A[i][a] = a + 1

    
    for j in range(2, len(numbers) - 2):
        for k in range(0, max_numb):
            if A[j][k] != 0:
                if (A[j - 2][k] == 0) and (A[j - 1][k] == 0) and (A[j + 1][k] == 0) and (A[j + 2][k] == 0):
                    count += 1
    
    print('#{} {}'.format(t, count))
