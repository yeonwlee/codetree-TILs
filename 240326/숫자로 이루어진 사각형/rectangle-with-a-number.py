from itertools import cycle


def print_rect(length_of_one_line: int) -> None:
    number_cycle = cycle(range(1, 10))
    for _ in range(length_of_one_line):
        line = [str(next(number_cycle)) for _ in range(length_of_one_line)]
        print(' '.join(line))

length_of_one_line: int = int(input())
print_rect(length_of_one_line)