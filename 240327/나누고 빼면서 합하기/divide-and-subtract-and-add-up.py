## index와 '번째'의 구분을 헷갈려하고 있음. 이걸 혼재해서 짠게 문제인 것으로 파악.


end_index_value:int = 1 # target_index 

def get_next_calculation_position(cur_index: int) -> int:    
    if cur_index % 2 == 0:
        return cur_index // 2
    else:
        return cur_index - 1


# 1번째 원소까지 값을 구한 다음에 그다음에 종료하나봄 + '번째'라는게 인덱스가 아님..
def calculate(number_arr: list[int], position_for_calculation: int) -> int:
    result:int = 0
    next_position: int = position_for_calculation
    while next_position > 0 :
        result += number_arr[next_position - 1]
        next_position = get_next_calculation_position(next_position)
    return result


num_of_arr, position_for_calculation = map(int, input().split())
number_arr = list(map(int, input().split()))

print(calculate(number_arr, position_for_calculation))