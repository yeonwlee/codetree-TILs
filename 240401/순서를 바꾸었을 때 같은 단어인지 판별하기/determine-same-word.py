word1 = list(input())
word2 = list(input())

word1.sort()
word2.sort()

print("Yes" if word1 == word2 else "No")