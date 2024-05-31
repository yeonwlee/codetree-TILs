source_str = input()
#  공백으로 구분하여 3의 배수 번째 문자열만 출력하는 프로그램을 작성해보세요.
print('\n'.join([word for index, word in enumerate(source_str.split(), start=1) if index % 3 == 0]))