max_num = int(input())
answers = []

def set_numbers(numbers:list[int]) -> None:
    if len(numbers) >= max_num:
        answers.append(numbers.copy())
        return
    for cur_num in range(1, max_num + 1):
        if cur_num in numbers:
            continue
        numbers.append(cur_num)
        set_numbers(numbers)
        numbers.pop()


for cur_num in range(1, max_num + 1):
    set_numbers([cur_num])

for answer in answers:
    print(' '.join(map(str, answer)))