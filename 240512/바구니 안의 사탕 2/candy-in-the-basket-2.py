num_of_basckets, plus_minus_pos = map(int, input().split())

basckets = [0] * 101 #바구니의 위치
for _ in range(num_of_basckets):
    num_of_candies, bascket_pos = map(int, input().split())
    bascket_pos -= 1 # 인덱스화
    basckets[bascket_pos] += num_of_candies

if plus_minus_pos >= 50: # 바구니 위치 1 ~ 100의 중앙
    print(sum(basckets))
else:
    end_index = plus_minus_pos * 2
    window_sum = sum(basckets[0:end_index + 1])
    max_sum = window_sum
    for index in range(1, len(basckets) - end_index):
        window_sum = window_sum - basckets[index - 1] + basckets[index + end_index]
        max_sum = max(window_sum, max_sum)

    print(max_sum)