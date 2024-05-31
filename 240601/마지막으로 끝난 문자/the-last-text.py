num_of_strs = int(input())

strs = [
    input()
    for _ in range(num_of_strs)
]

target_char = input()

filtered_words = [word for word in strs if word[-1] == target_char]
print(len(filtered_words))
print('\n'.join(filtered_words))