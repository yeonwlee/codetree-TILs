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

is_possible = False
for num_of_y_line in range(min(len(set_x_coord)+1, 4)): # 최소 set의 개수 만큼, 최대 3개
    x_coord_combies = list(combinations(set_x_coord, num_of_y_line)) # 해당 선분 수 만큼의 조합 만들기
    for cur_y_lines in x_coord_combies:
        # 해당 선분에서 덮어씌워질 점 외에, y좌표를 set으로 모음
        y_coord = {coords_dict['y'][index] for index, number in enumerate(coords_dict['x']) if number not in cur_y_lines}
        # 3개 선분 - x 좌표를 지우는 데 사용했던 선분의 수 - 남은 y 좌표를 지우는 데 필요한 선분의 수가 양수면
        if 3 - num_of_y_line - len(y_coord) >= 0:
            is_possible = True # 선분 3개로 지우기 가능
            break
if is_possible:
    print(1)
else:
    print(0)