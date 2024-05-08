def is_within_bound(row:int, col: int) -> bool:
    return 0 <= row < rect_width and 0 <= col < rect_width


def is_visited(row:int, col:int) -> bool:
    return rect[row][col] is not None
     

rect_width = int(input())

# 정사각형
rect = [
    [None for _ in range(rect_width)]
    for _ in range(rect_width)
]

# 안에서 바깥으로 채우는 문제 조건을 바깥에서 안으로 채우는 조건으로 치환. 
# 숫자를 반대로 채우기.
cur_row, cur_col = rect_width - 1, rect_width - 1
rect[cur_row][cur_col] = rect_width * rect_width
dir_index = 0
# 왼, 위, 오, 아래
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

for number in range(rect_width * rect_width - 1, 0, -1):
    while True:
        next_row, next_col = cur_row + directions[dir_index][0], cur_col + directions[dir_index][1]
        if is_within_bound(next_row, next_col) and not is_visited(next_row, next_col):
            cur_row, cur_col = next_row, next_col
            rect[cur_row][cur_col] = number
            break
        else:
            dir_index = (dir_index + 1) % 4


for row in rect:
    for col in row:
        print(col, end=' ')
    print()