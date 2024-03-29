def solution(nth: int, memory_dict:dict[int, int]=None) -> int:
    if memory_dict is None:
        memory_dict = {1:1, 2:2}

    if nth in memory_dict:
        return memory_dict[nth]
    else:
        return solution(nth // 3) + solution(nth - 1)


nth = int(input())
print(solution(nth))