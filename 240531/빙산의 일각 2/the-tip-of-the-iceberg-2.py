num_of_ice = int(input())

ice_height_info = [
    int(input())
    for _ in range(num_of_ice)
]

max_num_of_ice = 0
for sea_lavel in range(1, max(ice_height_info) - 1):
    ice = ''.join(['1' if ice_height > sea_lavel else '0' for ice_height in ice_height_info])
    max_num_of_ice = max(max_num_of_ice, sum(1 for cur_ice_piece in ice.split('0') if cur_ice_piece != ''))

print(max_num_of_ice)