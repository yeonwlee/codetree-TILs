#슬라이싱 사용시. 슬라이싱하면서 계속 객체를 만들기때문에 메모리 사용량이 높을 수 있음
# def get_start_index_part_of_source(source: str, target: str) -> int:
#     for index in range(len(source) - len(target) + 1):
#         if source[index: len(target) + index] == target:
#             return index
#     return None


# input_string = input() #기준 문자열
# target_string = input() #기준 문자열에서 부분 문자열로 존재하는지 확인할 문자열

# # if start_index:=get_start_index_part_of_source(input_string, target_string): # 이렇게 하면 start_index가 0인 경우 false로 인식해버림
# if (start_index:=get_start_index_part_of_source(input_string, target_string)) is not None:
#     print(start_index)
# else:
#     print(-1)


def get_start_index_part_of_source(source: str, target: str) -> int:
    if len(source) < len(target): #target이 부분문자열인게 불가
        return None
    for base_index in range(len(source)):
        for target_index in range(len(target)):
            if base_index + target_index < len(source):
                if source[base_index + target_index] != target[target_index]:
                    break
                if target_index == len(target) - 1:
                    return base_index
    return None


input_string = input() #기준 문자열
target_string = input() #기준 문자열에서 부분 문자열로 존재하는지 확인할 문자열

# if start_index:=get_start_index_part_of_source(input_string, target_string): # 이렇게 하면 start_index가 0인 경우 false로 인식해버림
if (start_index:=get_start_index_part_of_source(input_string, target_string)) is not None:
    print(start_index)
else:
    print(-1)