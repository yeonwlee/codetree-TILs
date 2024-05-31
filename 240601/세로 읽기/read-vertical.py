from itertools import zip_longest

words = [
    input()
    for _ in range(5)
]

for word in zip_longest(*words, fillvalue=''):
    print(''.join(word), end='')