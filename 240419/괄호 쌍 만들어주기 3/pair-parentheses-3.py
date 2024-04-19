source = input()
count_cases_of_valid_bracket = 0

for start_bracket_index, start_bracket in enumerate(source):
    if start_bracket == "(":
        for _, end_bracket in enumerate(source[start_bracket_index + 1:]):
            if end_bracket == ")":
                count_cases_of_valid_bracket += 1

print(count_cases_of_valid_bracket)