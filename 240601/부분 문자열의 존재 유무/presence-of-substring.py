source_str = input() # 알파벳 대소문자로만. 공백없음

print('YES' if source_str.find('ee') != -1 else 'NO', 'YES' if source_str.find('ea') != -1 else 'NO')