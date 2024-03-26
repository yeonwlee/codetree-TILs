length_of_one_line: int = int(input())


def print_rect(length_of_one_line: int) -> None:
    cur_num: int = 1
    for _ in range(length_of_one_line):
        count: int = 0
        while (count:= count + 1) <= length_of_one_line:
            print(cur_num, end=' ')
            cur_num += 1
            if cur_num > 9:
                cur_num = 1
        print()


print_rect(length_of_one_line)