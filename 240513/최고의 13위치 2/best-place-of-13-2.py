width_of_grid = height_of_grid = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(width_of_grid)
]

sum_grid = [[sum(row[i:i+3]) for i in range(width_of_grid - 2)] for row in grid]
max_num_of_coins = 0

for row_1 in range(height_of_grid):
    for col_1 in range(width_of_grid - 2):
        for row_2 in range(row_1, height_of_grid):
            start_col = col_1 + 3 if row_1 == row_2 else 0
            if start_col + 3 <= width_of_grid:   
                for col_2 in range(start_col, width_of_grid - 2): 
                    max_num_of_coins = max(max_num_of_coins, sum_grid[row_1][col_1]+sum_grid[row_2][col_2])
            else:
                continue
   

print(max_num_of_coins)