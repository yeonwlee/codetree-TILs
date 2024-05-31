'''
공백으로 구분하여 단어의 개수와 각 줄마다 단어를 출력하는 프로그램을 작성해보세요. 
단, 문자열은 공백으로 시작하지 않으며 두 단어 사이에는 공백이 한개만 들어갑니다.
'''

source: str = input()

words = source.split()
print(len(words))
print('\n'.join(words))