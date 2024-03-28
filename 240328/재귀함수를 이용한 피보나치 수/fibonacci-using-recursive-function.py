def nth_of_fibonacci(nth: int) -> None:
    if nth == 0:
        return 0
    elif nth == 1 or nth == 2:
        return 1
    
    return nth_of_fibonacci(nth - 2) + nth_of_fibonacci(nth - 1)


nth = int(input())
print(nth_of_fibonacci(nth))