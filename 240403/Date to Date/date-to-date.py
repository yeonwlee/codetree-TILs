month1, date1, month2, date2 = map(int, input().split())

date_in_month = [1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 1월 1일부터, 시작일 포함이므로 인덱스 0을 1로 줌
date_to_date = (sum(date_in_month[:month2 - 1]) + date2) - (sum(date_in_month[:month1 - 1]) + date1)

print(1 if date_to_date == 0 else date_to_date)