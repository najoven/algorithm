import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for t in range(1,T+1):
    num_cards = int(input())
    cards = input() # 문자열은 그냥 받아도 된다
    count_list = [0] * 10 # 0부터 9까지
    
    # cards를 정수로 받아오면?
    # for _ in range(num_cards):
    #     count_list[cards % 10] += 1
    #     cards = cards // 10
    
    for card in cards_list:
        count_list[int(card)] += 1

    max_idx = 0
    for j in range(1, len(count_list)):
        if count_list[max_idx] <= count_list[j]: # 어차피 오른쪽으로 가니까
            max_idx = j

    print('#{} {} {}'.format(t, max_idx, count_list[max_idx]))