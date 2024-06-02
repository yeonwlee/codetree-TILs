num_of_points = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(num_of_points)
]

min_x, min_y = float('inf'), float('inf')
max_x, max_y = float('-inf'), float('-inf')
for x, y in points:
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

min_largest_number_of_points = float('inf')
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        area_points = [0, 0, 0, 0]
        for region_x, region_y in points:
            if region_x < x and region_y > y:
                area_points[0] += 1
            elif region_x < x and region_y < y:
                area_points[1] += 1
            elif region_x > x and region_y < y:
                area_points[2] += 1
            else:
                area_points[3] += 1
        min_largest_number_of_points = min(min_largest_number_of_points, max(area_points))

print(min_largest_number_of_points)