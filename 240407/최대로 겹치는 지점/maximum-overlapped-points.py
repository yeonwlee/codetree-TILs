num_of_lines = int(input())
point_info = [0 for _ in range(101)] # 1 ~ 100
lines = [
    tuple(map(int, input().split()))
    for _ in range(num_of_lines)
]

for x1, x2 in lines:
    for index in range(x1 - 1, x2):
        point_info[index] += 1

print(max(point_info))