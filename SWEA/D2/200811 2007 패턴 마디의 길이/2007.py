import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    words = str(input())

    pattern = ''
    for i in range(0, len(words)-1):
        breaker = 0
        for j in range(i+1, len(words)-1):
            if (words[i] == words[j]) and (words[i+1] == words[j+1]):
                a = i
                b = j
                breaker = 1
                break
        if breaker == 1:
            break

    for k in range(a, b):
        pattern += words[k]

    print('#{} {}'.format(t, len(pattern)))