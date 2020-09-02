import sys; sys.stdin = open('sample_input.txt', 'r')

def numbers(cardsdict):
    for card in cardtypes:
        if len(cardsdict[card]) != len(set(cardsdict[card])):
            result = 'ERROR'
            return result
        else:
            resultdict[card] = 13 - len(cardsdict[card])
    return '{} {} {} {}'.format(resultdict['S'], resultdict['D'], resultdict['H'], resultdict['C'])

for tc in range(1, int(input())+1):
    cards = input()
    N = len(cards)
    cardtypes = ['S', 'D', 'H', 'C']
    cardsdict = {'S' : [], 'D' : [], 'H' : [], 'C' : []}
    resultdict = {'S': 0, 'D': 0, 'H': 0, 'C': 0}
    for i in range(0, N, 3):
        cardsdict[cards[i]].append(int(cards[i+1]+cards[i+2]))

    print('#{} {}'.format(tc, numbers(cardsdict)))


