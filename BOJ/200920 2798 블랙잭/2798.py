import sys; sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
cards = list(map(int, input().split()))
diff = [abs(sum(cards)-M)]
results = [sum(cards)]

def subset(k, cur_sum, cnt):
    if cnt == 3:
        dif = diff.pop(0)
        result = results.pop(0)
        if M - cur_sum >= 0 and dif > M - cur_sum:
            diff.append(M-cur_sum)
            results.append(cur_sum)
        else:
            diff.append(dif)
            results.append(result)
        return
    if k == N: return
    else:
        subset(k+1, cur_sum + cards[k], cnt + 1)
        subset(k+1, cur_sum, cnt)

subset(0, 0, 0)
print(results[0])