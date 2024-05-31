'''
알파벳으로 이루어져 있고 공백을 포함한 10개의 문자열이 주어지면 
공백으로 구분하여 짝수 번째 문자열만 출력하는 프로그램을 작성해보세요.
'''

print('\n'.join(word for nth, word in enumerate(input().split(), start=1) if nth % 2 == 0))