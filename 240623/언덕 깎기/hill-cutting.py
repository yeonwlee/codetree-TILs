import sys

input = sys.stdin.readline

num_of_hill = int(input().rstrip())

hills = [
    int(input().rstrip())
    for _ in range(num_of_hill)
]

# 가장 높은 언덕과 가장 낮은 언덕의 높이차가 17 이하가 되도록 만들어야 할 때, 
# 들어가는 최소 비용을 구하는 프로그램을 작성해보세요.

# 0 ≤ 언덕의 높이 ≤ 100

hills.sort()
low_hill, high_hill = hills[0], hills[-1]

min_cost = float('inf')
if high_hill - low_hill > 17:
    for height in range(high_hill - 17):
        min_height = height
        max_height = height + 17
        current_cost = 0

        for hill in hills:
            if hill < min_height:
                current_cost += (min_height - hill) ** 2 # 올리기
            elif hill > max_height:
                current_cost += (max_height - hill) ** 2 # 내리기
            
        min_cost = min(min_cost, current_cost)
else:
    min_cost = 0
    
print(min_cost)