def check_rect_inner(coord, rect, check_to = 1) -> None:
    x1, y1, x2, y2 = rect
    for row_index in range(x1, x2):
        for col_index in range(y1, y2):
            coord[row_index][col_index] = check_to


rect1 = tuple(map(int, input().split()))
rect2 = tuple(map(int, input().split()))
cover_rect = tuple(map(int, input().split()))

coord = [
    [0 for _ in range(2000)] 
    for _ in range(2000)
]

check_rect_inner(coord, rect1)
check_rect_inner(coord, rect2)
check_rect_inner(coord, cover_rect, 0)

print(sum(1 for row in coord for col in row if col >= 1))