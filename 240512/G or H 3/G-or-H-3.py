num_of_person, size_of_picture = map(int, input().split())

person = [0] * 100 # 최대 사람 수

first_position = float('inf')
last_position = float('-inf')
for _ in range(num_of_person):
    person_position, point = input().split()
    person_position = int(person_position) - 1 # index 화 
    first_position = min(person_position, first_position)
    last_position = max(person_position, last_position)
    if point == 'G':
        person[person_position] = 1
    elif point == 'H':
        person[person_position] = 2

max_points = float('-inf')
for index in range(first_position, last_position - size_of_picture + 1):
    cur_range_points = 0
    for cur_index in range(index, index + size_of_picture + 1):
        cur_range_points += person[cur_index]
    max_points = max(max_points, cur_range_points)


print(max_points)