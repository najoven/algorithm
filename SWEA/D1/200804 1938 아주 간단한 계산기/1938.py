import sys
sys.stdin = open('input.txt', 'r')

T = list(map(int, input().split()))

i = T[0]
j = T[1]

sum_ij = i + j
sub_ij = i - j
mul_ij = i * j
div_ij = i // j

print(sum_ij)
print(sub_ij)
print(mul_ij)
print(div_ij)