## 서 있는 위치도 오름차, 키도 오름차인 
#서로 다른 쌍 구하기

#소의 위치 오름차인 경우를 살피면서, 그 소의 키들을 곧바로 비교해보기
#서로 다른 쌍
num_of_cow = int(input())

cow_height_info = list(map(int, input().split()))
asc_cow_count = 0

for first_cow_index in range(len(cow_height_info)):
    for second_cow_index in range(first_cow_index + 1, len(cow_height_info)):
        for third_cow_index in range(second_cow_index + 1, len(cow_height_info)):
            if cow_height_info[first_cow_index] <= cow_height_info[second_cow_index] <= cow_height_info[third_cow_index]:
                asc_cow_count += 1

print(asc_cow_count)