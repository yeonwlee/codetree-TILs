import math

def get_lcm(num1: int, num2: int) -> int:
    return (num1 * num2) // math.gcd(num1, num2)


def recursive_lcm(numbers: list[int]) -> int:
    first_num = numbers[0]
    if len(numbers) == 1:
        return first_num
    rest_numbers = recursive_lcm(numbers[1:])
    return get_lcm(first_num, rest_numbers)
    

num_of_numbers = int(input())
numbers = list(map(int, input().split()))

print(recursive_lcm(numbers))