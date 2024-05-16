num_of_points = int(input())

points = [
    tuple(map(int, input().split()))
    for _ in range(num_of_points)
]

# 한 변은 x축에 평행, 다른 한 변은 y축에 평행한 삼각형
# -> (x1, y1) , (x2, y2), (x3, y3) -> ex. x1=x3, y1=y2

max_area = 0

for first in range(len(points)):
    x1, y1 = points[first]
    for second in range(len(points) - 1):
        x2, y2 = points[second]
        for third in range(len(points) - 2):
            x3, y3 = points[third]
            if len(set([x1, x2, x3])) == 2 and len(set([y1, y2, y3])) == 2:
                max_area = max(max_area, 
                            (abs(max([x1, x2, x3]) - min([x1, x2, x3]))) * abs((max([y1, y2, y3]) - min([y1, y2, y3])))
                        )
            

print(max_area)