source: str = input()

for index, char in enumerate(source):
    for start_index in range(index, len(source)):
        print(source[start_index], end='')
    print(source[:index])
print(source)