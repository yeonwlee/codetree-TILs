from bisect import bisect_left # 이진 탐색


def find_nearest_alphabet_distance(cur_pos:int, target:str) -> int:
    alphabet_positions = alphabet_pos_info[target]
    compare_pos = bisect_left(alphabet_positions, cur_pos)

    if compare_pos == 0:
        return abs(cur_pos - alphabet_positions[0])
    elif compare_pos == len(alphabet_positions):
        return abs(cur_pos - alphabet_positions[-1])
    else:
        return min(abs(cur_pos - alphabet_positions[compare_pos - 1]), abs(cur_pos - alphabet_positions[compare_pos]))


num_of_alphabets, x1, x2 = map(int, input().split())

alphabet_pos_info = {'S':[], 'N':[]}

for _ in range(num_of_alphabets):
    alphabet, position = input().split()
    alphabet_pos_info[alphabet].append(int(position))

for alphabet, positions in alphabet_pos_info.items():
    alphabet_pos_info[alphabet] = sorted(positions)

num_of_special_position = 0
for cur_checking_pos in range(x1, x2 + 1):
    if find_nearest_alphabet_distance(cur_checking_pos, 'S') <= find_nearest_alphabet_distance(cur_checking_pos, 'N'):
        num_of_special_position += 1

print(num_of_special_position)