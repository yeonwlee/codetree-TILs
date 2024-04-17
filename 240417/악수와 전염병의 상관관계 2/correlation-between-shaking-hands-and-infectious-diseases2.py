num_of_person, num_of_effective_infections, first_infected_person, num_of_handshaking = map(int, input().split())

handshaking_info = [
    tuple(map(int, input().split()))
    for _ in range(num_of_handshaking)
]

handshaking_info.sort(key=lambda x:x[0]) #전체 입력 개수가 많지 않으므로, 시간 순으로 정렬을 해줌

infected_person_info = [0] * num_of_person
infected_person_info[first_infected_person -1 ] = 1

effective_infections_info = [num_of_effective_infections] * num_of_person

#감염된 사람들끼리 악수한 경우, 둘 다 유효한 감염횟수를 차감시켜야함
for handshaking in handshaking_info:
    _, person_x, person_y = handshaking
    if infected_person_info[person_x - 1] and effective_infections_info[person_x - 1] > 0:
        infected_person_info[person_y - 1] = 1
        effective_infections_info[person_x - 1] -= 1
    if infected_person_info[person_y - 1] and effective_infections_info[person_y - 1] > 0:
        infected_person_info[person_x - 1] = 1
        effective_infections_info[person_y - 1] -= 1


print(''.join(map(str, infected_person_info)))