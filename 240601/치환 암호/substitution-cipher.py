encrypted_str = input() # 암호화된 문자열은 소문자 또는 띄어쓰기로만 이루어져 있습니다.
rule = input()

base_ascii = ord('a')
decrypted_dict = {char:chr(base_ascii + index) for index, char in enumerate(rule)}
print(''.join([decrypted_dict[char] if char != ' ' else ' ' for char in encrypted_str]))