source = input()

count_of_koi = 0
count_of_ioi = 0

for index in range(len(source) - 2):
    cur_word = source[index: index + 3]
    if cur_word == 'KOI':
        count_of_koi += 1
    elif cur_word == 'IOI':
        count_of_ioi += 1

print(count_of_koi, count_of_ioi)