num_of_lines = int(input())

lines = [
    tuple(map(int, input().split()))
    for _ in range(num_of_lines)
]


count = 0
for first_index in range(len(lines) - 2):
    for second_index in range(first_index + 1, len(lines) - 1):
        for third_index in range(second_index + 1, len(lines)):
            rest_of_lines = [lines[index] for index in range(len(lines)) if index not in {first_index, second_index, third_index}]
            is_available = True
            for cur_line_index in range(len(rest_of_lines)):
                start, end = rest_of_lines[cur_line_index]
                for compare_line_index in range(len(rest_of_lines)):
                    if cur_line_index != compare_line_index:
                        start2, end2 = rest_of_lines[compare_line_index]
                        if start <= start2 <= end or start <= end2 <= end:
                            is_available = False
                            break
                if not is_available:
                    break
            if is_available:
                count += 1

print(count)