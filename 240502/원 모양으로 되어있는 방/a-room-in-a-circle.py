num_of_rooms = int(input())

# 각 방에 몇 명이 들어가야하는지 나타내는 정보
room_info = [
    int(input())
    for _ in range(num_of_rooms)
]

whole_person = sum(room_info)
distances = [0 for _ in range(num_of_rooms)]

for start_room_index in range(num_of_rooms):
    remain_person = whole_person
    for cur_room_index in range(start_room_index, start_room_index + num_of_rooms):
        remain_person -= room_info[(cur_room_index + num_of_rooms) % num_of_rooms]
        distances[start_room_index] += remain_person


print(min(distances))