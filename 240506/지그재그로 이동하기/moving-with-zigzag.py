start_position, end_position = map(int, input().split())
pow_value = 0
moving_distance = 0
cur_position = start_position

while cur_position != end_position:
    if pow_value % 2 == 0: 
        next_position = start_position + pow(2, pow_value)   
    else:
        next_position = start_position - pow(2, pow_value)   

    for _ in range(abs(cur_position - next_position)):
        moving_distance += 1
        if pow_value % 2 == 0: 
            cur_position += 1
        else:
            cur_position -= 1
        if cur_position == end_position:
            break
    pow_value += 1

print(moving_distance)