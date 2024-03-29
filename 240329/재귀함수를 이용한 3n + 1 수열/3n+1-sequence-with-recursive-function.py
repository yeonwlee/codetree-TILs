def count_making_one(number: int) -> int:
    if number == 1:
        return 0 # 목표 수에 도달해 횟수를 세지 않음

    cur_calculated_value = (number // 2 if number % 2 == 0 else number * 3 + 1)
    return count_making_one(cur_calculated_value) + 1


number = int(input())
print(count_making_one(number))