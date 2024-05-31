chars:list[str] = input().split()

chars.sort() # 작은 값과 큰 값을 구분하기 위함
print(ord(chars[0]) * ord(chars[1]),ord(chars[-1]) % ord(chars[0]))