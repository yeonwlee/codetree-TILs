'''
왼쪽부터 순서대로 보며 단어에 맞는 부분을 찾아 지웁니다.
해당 단어가 지워진 이후 문자열은 다시 남은 부분끼리 붙게되고, 
다시 처음부터 순서대로 보며 더 이상 지울 단어가 없을 때까지 이 과정을 반복합니다.
'''

words = input()
delete_word = input()

while (del_word_index:=words.find(delete_word)) != -1:
    words = words[:del_word_index] + words[del_word_index+len(delete_word):]

print(words)