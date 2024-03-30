num_of_words = int(input())
words = [
    input()
    for _ in range(num_of_words)
]

words.sort()

for word in words:
    print(word)