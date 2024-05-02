length_of_source_str = int(input())
source = input()

count_C = 0
count_CO = 0
count_COW = 0

# target: COW
for index, letter in enumerate(source):
    if letter == "C":
        count_C += 1
    elif letter == "O":
        count_CO += count_C
    elif letter == "W":
        count_COW += count_CO

print(count_COW)