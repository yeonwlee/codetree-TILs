def print_gugudan(num1:int, middle_num:int, num2:int) -> None:
    for cur_dan in range(num1, num2 + 1):
        if cur_dan == middle_num:
            continue
        for cur_multiply_value in range(1, 10):
            print(f"{cur_dan} * {cur_multiply_value} = {cur_dan * cur_multiply_value}")


numbers = list(map(int, input().split()))
numbers.sort()

print_gugudan(numbers[0], numbers[1], numbers[2])