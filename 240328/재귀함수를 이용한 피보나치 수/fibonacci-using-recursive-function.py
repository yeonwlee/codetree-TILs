# def nth_of_fibonacci(nth: int) -> None:
#     elif nth <= 2:
#         return 1
    
#     return nth_of_fibonacci(nth - 2) + nth_of_fibonacci(nth - 1)

def nth_of_fibonacci(nth: int, info:dict=None) -> None:
    if info is None:
        info = {1:1, 2:1}
    
    if nth in info:
        return info[nth]

    return nth_of_fibonacci(nth - 2, info) + nth_of_fibonacci(nth - 1, info)


nth = int(input())
print(nth_of_fibonacci(nth))