plus = '+'
sharp = '#'
add = ''

for i in range(0, 5):
    for j in range(0, 5):
        if i == j:
            add += sharp
        else:
            add += plus
    print(add)
    add = ''