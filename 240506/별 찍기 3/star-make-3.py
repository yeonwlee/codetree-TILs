num_of_lines = int(input())
middle_line = num_of_lines // 2
answers = []
for cur_line in range(middle_line + 1):
    cur_line_stars = " " * cur_line + "*" + "*" * (cur_line * 2)
    print(cur_line_stars)
    answers.append(cur_line_stars)

for answer in answers[len(answers) - 2::-1]:
    print(answer)