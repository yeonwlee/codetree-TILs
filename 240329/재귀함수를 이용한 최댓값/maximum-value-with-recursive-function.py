def get_max_value(numbers: list[int], index_of_list: int) -> int:
    if index_of_list == 0:
        return numbers[index_of_list]

    compare_value = get_max_value(numbers, index_of_list - 1)
    return (compare_value if numbers[index_of_list] < compare_value else numbers[index_of_list])


num_of_numbers = int(input())
numbers = list(map(int, input().split()))
print(get_max_value(numbers, num_of_numbers - 1))