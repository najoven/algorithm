import sys
sys.stdin = open('input.txt', 'r')

T = str(input())
alpha_dict = {}
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

i = 1
for letter in letters:
    alpha_dict[letter] = i
    i += 1

for t in T:
    print('{}'.format(alpha_dict[t]), end = ' ')