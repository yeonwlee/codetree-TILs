num_of_numbers = int(input())
# numbers = [
#     int(input())
#     for _ in range(num_of_numbers)
# ]

numbers = [int(input())]
longest_continued_asc_count = cur_continued_asc_count = 1

for _ in range(1, num_of_numbers):
    numbers.append(int(input()))
    if numbers[-2] < numbers[-1]:
        cur_continued_asc_count += 1
    else: #연속적으로 커지지 않은 경우
        if longest_continued_asc_count < cur_continued_asc_count:
            longest_continued_asc_count = cur_continued_asc_count
        cur_continued_asc_count = 1

if longest_continued_asc_count < cur_continued_asc_count:
    longest_continued_asc_count = cur_continued_asc_count
     
print(longest_continued_asc_count)