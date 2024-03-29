def sum_all_range_of_same_type_number(number: int) -> int: 
    if number == 1 or number == 2:
        return number
    
    return number + sum_all_range_of_same_type_number(number - 2)


number = int(input())
print(sum_all_range_of_same_type_number(number))