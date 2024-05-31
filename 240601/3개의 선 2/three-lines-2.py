from collections import defaultdict
from itertools import combinations

num_of_coord = int(input())

coords = [
    tuple(map(int, input().split()))
    for _ in range(num_of_coord)
]

coords_dict = defaultdict(list)
for coord in coords:
    coords_dict['x'].append(coord[0])
    coords_dict['y'].append(coord[1])

set_x_coord = set(coords_dict['x'])
set_y_coord = set(coords_dict['y'])

list_x_coord_not_dupled = list(set_x_coord)

is_possible = False
for num_of_y_line in range(len(list_x_coord_not_dupled)):
    x_coord_combies = list(combinations(set_x_coord, num_of_y_line))
    for cur_y_lines in x_coord_combies:
        y_coord = {coords_dict['y'][index] for index, number in enumerate(coords_dict['x']) if number not in cur_y_lines}
        if 3 - (num_of_y_line + len(y_coord)) >= 0:
            is_possible = True
            break
if is_possible:
    print(1)
else:
    print(0)