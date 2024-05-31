num_of_exchange = int(input())

exchange_info = [
    tuple(map(int, input().split()))
    for _ in range(num_of_exchange)
]

max_points = 0
# 조약돌을 처음에 어디에(1~3) 넣어야가장 높은 점수를 얻을 수 있을지
for nth in range(3):
    cups = [1 if cup == nth else 0 for cup in range(3)]
    cur_points = 0
    for a, b, c in exchange_info:
        cups[a - 1], cups[b - 1] = cups[b - 1], cups[a - 1]
        if cups[c - 1] == 1:
            cur_points += 1
    max_points = max(max_points, cur_points)

print(max_points)