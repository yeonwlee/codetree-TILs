# 알파벳으로 이루어진 4개의 문자열이 주어지면 입력받은 거꾸로, 역순으로 출력하는 프로그램을 작성해보세요.

# 그냥 재귀 연습
def print_word_reverse(num_of_words:int) -> None:
    if num_of_words == 4:
        return
    word = input()
    print_word_reverse(num_of_words + 1)
    print(word[::-1])


print_word_reverse(0)