from itertools import cycle

def is_within_rect(row: int, col: int) -> bool:
    return 0 <= row < num_of_rows and 0 <= col < num_of_cols


num_of_rows, num_of_cols = map(int, input().split())
rect = [
    [None for _ in range(num_of_cols)]
    for _ in range(num_of_rows)
]

cur_direction_index = 0
cur_row, cur_col = 0, 0
#오른쪽, 아래, 왼쪽, 위 # 시계방향 90도 회전
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
alphabet_gen = cycle(map(chr, range(ord('A'), ord('Z') + 1))) # 26자. 순환 제너레이터
rect[0][0] = next(alphabet_gen)


for _ in range(2, num_of_rows * num_of_cols + 1):
    while True:
        next_row, next_col = cur_row + directions[cur_direction_index][0], cur_col + directions[cur_direction_index][1]
        if is_within_rect(next_row, next_col) and rect[next_row][next_col] is None:
            cur_row, cur_col = next_row, next_col
            rect[cur_row][cur_col] = next(alphabet_gen)
            break
        else:
            cur_direction_index = (cur_direction_index + 1) % 4


for row in rect:
    for col in row:
        print(col, end=' ')
    print()