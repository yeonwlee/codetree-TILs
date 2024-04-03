def day_to_minute(date: int) -> int:
    return date * 24 * 60


def hour_to_minute(hour: int) -> int:
    return hour * 60


date, hour, minute = map(int, input().split())

base_date_time_to_minute = day_to_minute(11) + hour_to_minute(11) + 11
compare_date_time_to_minute = day_to_minute(date) + hour_to_minute(hour) + minute

print(-1 if base_date_time_to_minute > compare_date_time_to_minute else compare_date_time_to_minute - base_date_time_to_minute)