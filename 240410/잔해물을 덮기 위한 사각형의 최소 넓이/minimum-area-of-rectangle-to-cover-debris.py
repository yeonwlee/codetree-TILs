OFFSET = 1000

def mark_rect_area(area: list, rect: tuple, mark: int) -> None:
    x1, y1, x2, y2 = list(map(lambda x: x + OFFSET, rect))
    for row in range(x1, x2):
        for col in range(y1, y2):
            area[row][col] = mark


rect1 = tuple(map(int, input().split()))
rect2 = tuple(map(int, input().split()))

area = [
    [0 for _ in range(2000)] for _ in range(2000)
]

mark_rect_area(area, rect1, 1)
mark_rect_area(area, rect2, 0)

x1, y1, x2, y2 = list(map(lambda x: x + OFFSET, rect1))
marked_x = []
marked_y = []
for row in range(x1, x2):
    for col in range(y1, y2):
        if area[row][col]:
            marked_x.append(row)
            marked_y.append(col)

minx, maxx = 0, 0
miny, maxy = 0, 0
if marked_x:
    marked_x.sort()
    marked_y.sort()
    minx, maxx = marked_x[0], marked_x[-1] + 1
    miny, maxy = marked_y[0], marked_y[-1] + 1

print((maxx - minx) * (maxy - miny))