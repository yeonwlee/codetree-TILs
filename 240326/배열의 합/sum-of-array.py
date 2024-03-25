arr = [
    sum(map(int, input().split()))
    for _ in range(4)
]
for sum_of_cur_row in arr:
    print(sum_of_cur_row)