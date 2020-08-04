import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for t in range(1,T+1):
    num_cards = int(input())
    cards = str(input())
    cards_list = []
    for card in cards:
        cards_list += [int(card)]

    count_list = [0] * (max(cards_list) +1)

    for card in cards_list:
        count = 0
        for i in cards_list:
            if card == i:
                count += 1
        count_list[card] = count

    max_count = count_list[0]
    max_idx = 0
    for j in range(0, len(count_list)):
        if count_list[j] > max_count:
            max_count = count_list[j]
            max_idx = j
        elif max_count == count_list[j]:
            if max_idx <= j:
                max_idx = j

    print('#{} {} {}'.format(t, max_idx, max_count))
    
