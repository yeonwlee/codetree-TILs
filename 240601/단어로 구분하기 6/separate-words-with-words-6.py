source_str = input()
print('\n'.join([word for index, word in enumerate(source_str.split(), start=1) if index % 3 == 0]))