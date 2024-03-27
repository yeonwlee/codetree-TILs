def get_start_index_part_of_source(source: str, target: str) -> int:
    for index in range(len(source) - len(target) + 1):
        if source[index: len(target) + index] == target:
            return index
    return None


input_string = input() #기준 문자열
target_string = input() #기준 문자열에서 부분 문자열로 존재하는지 확인할 문자열

if start_index:=get_start_index_part_of_source(input_string, target_string):
    print(start_index)
else:
    print(-1)