def sum_each_position(number:int) -> int:
    if number < 10: #1의자리
        return number 
    
    cur_position_value = number % 10 
    return cur_position_value + sum_each_position(number // 10)


num1, num2, num3 = map(int, input().split())
print(sum_each_position(num1 * num2 * num3))