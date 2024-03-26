row, col = map(int, input().split())


def print_lines(row: int, col:int) -> None:
    for _ in range(row):
        print("1" * col)

print_lines(row, col)