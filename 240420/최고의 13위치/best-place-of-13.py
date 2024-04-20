width_of_grid = int(input())
max_num_of_coins_in_area = 0

for _ in range(width_of_grid):
    cur_row_coins = list(map(int, input().split()))
    for first_index_of_area in range(len(cur_row_coins) - 2):
        cur_coins_in_area = sum(1 for position in cur_row_coins[first_index_of_area: first_index_of_area + 3] if position == 1)
        max_num_of_coins_in_area = max(max_num_of_coins_in_area, cur_coins_in_area)

print(max_num_of_coins_in_area)