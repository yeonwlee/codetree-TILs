# # 풀이1: str 활용해서 풀기
# num_of_ice = int(input())

# ice_height_info = [
#     int(input())
#     for _ in range(num_of_ice)
# ]

# max_num_of_ice = 0
# # 해수면 레벨
# for sea_lavel in range(1, max(ice_height_info) - 1):
#     #해수면보다 높으면 '1', 낮으면 '0'으로 변경후 str 화
#     ice = ''.join(['1' if ice_height > sea_lavel else '0' for ice_height in ice_height_info])
#     max_num_of_ice = max(max_num_of_ice, sum(1 for cur_ice_piece in ice.split('0') if cur_ice_piece != ''))

# print(max_num_of_ice)


# 풀이2: 
num_of_ice = int(input())

ice_height_info = [
    int(input())
    for _ in range(num_of_ice)
]

max_num_of_ice = 1
# 해수면 레벨
for sea_level in range(1, max(ice_height_info) - 1):
    cur_num_of_ice = 0
    for ice_index in range(1, len(ice_height_info)):
        if ice_height_info[ice_index] < sea_level:
            cur_num_of_ice += 1
    max_num_of_ice = max(max_num_of_ice, cur_num_of_ice)

print(max_num_of_ice)