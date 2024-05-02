length_of_source_str = int(input())
source = input()

start_letter = 0
completed_middle_letter = 0
completed_all = 0

# target: COW
for index, letter in enumerate(source):
    if letter == "C":
        start_letter += 1
    elif letter == "O":
        completed_middle_letter += start_letter
    elif letter == "W":
        completed_all += completed_middle_letter

print(completed_all)