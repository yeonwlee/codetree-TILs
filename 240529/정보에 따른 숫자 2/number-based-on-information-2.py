def find_nearest_alphabet_position(cur_pos:int, target:str) -> int:
    return min(abs(cur_pos - alphabet_pos) for alphabet_pos in alphabet_pos_info[target])


num_of_alphabets, x1, x2 = map(int, input().split())

alphabet_pos_info = {'S':[], 'N':[]}

for _ in range(num_of_alphabets):
    alphabet, position = input().split()
    alphabet_pos_info[alphabet].append(int(position))

for alphabet, positions in alphabet_pos_info.items():
    alphabet_pos_info[alphabet] = sorted(positions)

num_of_special_position = 0
for cur_checking_pos in range(x1, x2 + 1):
    if find_nearest_alphabet_position(cur_checking_pos, 'S') <= find_nearest_alphabet_position(cur_checking_pos, 'N'):
        num_of_special_position += 1

print(num_of_special_position)