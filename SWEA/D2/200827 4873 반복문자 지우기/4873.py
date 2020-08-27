import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    wordl = input()
    words = []
    for word in wordl:
        words += [word]

    i = 0
    while 1:
        if i == len(words) - 1:
            break
        j = i + 1
        if words[i] == words[j]:
            words = words[:i] + words[j+1:]
            i = 0
        else:
            i += 1

    print('#{} {}'.format(t, len(words)))


