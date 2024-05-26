def set_numbers(cur_answer:list[int]):
    if len(cur_answer) == num_of_choice:
        if len(cur_answer) == 1:
            print(cur_answer[-1], cur_answer[-1])
        else:
            print(' '.join(map(str, cur_answer)))
        return
    for num in range(1, maximum_value + 1):
        cur_answer.append(num)
        set_numbers(cur_answer)
        cur_answer.pop()
    

num_of_choice, maximum_value = map(int, input().split())

for num in range(1, maximum_value + 1):
    set_numbers([num])