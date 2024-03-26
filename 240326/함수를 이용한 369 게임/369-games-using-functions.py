a, b = map(int, input().split())


# #3, 6, 9 를 가지고 있는지 확인
# def has_target_num(num: int) -> bool:
#     while num > 0:
#         cur_position_num = num % 10
#         if cur_position_num == 3 or cur_position_num == 6 or cur_position_num == 9:
#             return True
#         num //= 10
#     return False


# def is_muitiple_value_of_3(num: int) -> bool:
#     return num % 3 == 0


# count: int = 0
# for cur_num in range(a, b + 1):
#     if has_target_num(cur_num) or is_muitiple_value_of_3(cur_num):
#         count += 1

# print(count)

def has_num_3_6_9(num: int) -> bool:
    return any(char in '369' for char in str(num))


def is_muitiple_of_3(num: int) -> bool:
    return num % 3 == 0

count: int = sum(1 for cur_num in range(a, b + 1) if is_muitiple_of_3(cur_num) or has_num_3_6_9(cur_num))
print(count)