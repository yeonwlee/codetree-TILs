source = input()

count_of_making_answer = 0

# for start_index in range(0, len(source)- 2):
#     if source[start_index: start_index + 2] == "((":
#         for end_index in range(start_index + 2, len(source) - 1):
#             if source[end_index: end_index + 2] == "))":
#                 count_of_making_answer += 1

# print(count_of_making_answer)



## 수를 누적해서 확인
open_count = 0
for i in range(len(source) - 1):
    if source[i:i+2] == '((':
        open_count += 1
    if source[i:i+2] == '))' and open_count > 0:
        count_of_making_answer += open_count

print(count_of_making_answer)