month1, date1, month2, date2 = map(int, input().split())

date_in_month = [1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 1월 1일부터 날짜를 세기 때문에 인덱스 0 을 1로 둠
date_to_date = (sum(date_in_month[:month2]) + date2 + 1) - (sum(date_in_month[:month1]) + date1)

print(date_to_date)