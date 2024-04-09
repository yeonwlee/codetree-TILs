OFFSET = 1000

def draw_rect_in_area(area_info: list, rect: tuple, symbol: int = 1) -> None:
    x1, y1, x2, y2 = rect
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
    for row in range(x1, x2):
        for col in range(y1, y2):
            area_info[row][col] = symbol


rect1 = tuple(map(int, input().split()))
rect2 = tuple(map(int, input().split()))

area = [
    [0 for _ in range(2000)] for _ in range(2000)
]

draw_rect_in_area(area, rect1)
draw_rect_in_area(area, rect2, 0) #rect2의 영역만큼 초기화

x1, y1, x2, y2 = rect1
x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
remained_x = []
remained_y = []
for row in range(x1, x2):
    for col in range(y1, y2):
        if area[row][col] == 1:
            remained_x.append(row)
            remained_y.append(col)

minx, maxx = remained_x[0], remained_x[-1] + 1 #1을 더해줘야 선분 길이가 나옴
miny, maxy = remained_y[0], remained_y[-1] + 1
print((maxx - minx) * (maxy - miny))