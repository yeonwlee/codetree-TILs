source = input()

count_of_making_answer = 0

for start_index in range(0, len(source)- 2):
    if source[start_index: start_index + 2] == "((":
        for end_index in range(start_index + 2, len(source) - 1):
            if source[end_index: end_index + 2] == "))":
                count_of_making_answer += 1

print(count_of_making_answer)