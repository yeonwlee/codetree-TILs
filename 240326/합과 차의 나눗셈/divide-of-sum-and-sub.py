a, b = map(int, input().split())
rounded_value = round((a+b)/(a-b), 2)
print(f"{rounded_value:.2f}")