from collections import defaultdict

char = input()
answer_dict = defaultdict(lambda: 'Failure', {'S': 'Superior', 'A': 'Excellent', 'B': 'Good', 'C': 'Usually', 'D':'Effort'})

print(answer_dict[char])