num_of_words, nth, string = input().split()

words =[
    input()
    for _ in range(int(num_of_words))
]

words_has_string = [word for word in words if word.startswith(string)]
words_has_string.sort()

print(words_has_string[int(nth) - 1])