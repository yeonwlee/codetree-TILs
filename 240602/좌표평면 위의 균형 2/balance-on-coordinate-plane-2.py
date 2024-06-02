num_of_points = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(num_of_points)
]

min_largest_number_of_points = float('inf')
for x in range(1, 101):
    for y in range(1, 101):
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