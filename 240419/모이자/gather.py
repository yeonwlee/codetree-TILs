#모든 사람들의 이동거리의 합이 최소가 되도록

num_of_houses = int(input())
house_person_info = list(map(int, input().split()))

min_moving_distance = float('inf')

for target_house_index, num_of_person_in_target_house in enumerate(house_person_info):
    moving_distance = 0
    for start_house_index, num_of_person_in_start_house in enumerate(house_person_info):
        if target_house_index != start_house_index:
            moving_distance = moving_distance + (abs(target_house_index - start_house_index) * num_of_person_in_start_house)
    if moving_distance < min_moving_distance:
        min_moving_distance = moving_distance

print(min_moving_distance)