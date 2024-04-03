def day_to_minute(date: int) -> int:
    return date * 24 * 60


def hour_to_minute(hour: int) -> int:
    return hour * 60


days, hour, minute = map(int, input().split())

base_date_time_to_minute = day_to_minute(11) + hour_to_minute(11) + 11
compare_date_time_to_minute = day_to_minute(days) + hour_to_minute(hour) + minute
time_diffrence = compare_date_time_to_minute - base_date_time_to_minute

print(-1 if base_date_time_to_minute > compare_date_time_to_minute else time_diffrence)