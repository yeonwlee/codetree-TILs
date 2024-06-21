a_math_score, a_english_score = map(int, input().split()) 
b_math_score, b_english_score = map(int, input().split()) 

if (a_math_score > b_math_score and 
    a_english_score > b_english_score):
    print(1)
else:
    print(0)