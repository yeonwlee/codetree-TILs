def print_hello_world(cur_row: int) -> None:
    if cur_row < 1:
        return
    print_hello_world(cur_row - 1)
    print("HelloWorld")


num_of_calls = int(input())
print_hello_world(num_of_calls)