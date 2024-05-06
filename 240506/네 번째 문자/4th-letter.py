num_of_strs, target_char = input().split()
num_of_strs = int(num_of_strs)
answers = []

for _ in range(num_of_strs):
    cur_str = input()
    if cur_str[3] == target_char:
        answers.append(cur_str)

print(len(answers))
for answer in answers:
    print(answer)