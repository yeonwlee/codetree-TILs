a, b, c = map(int, input().split())


def get_min_value(*args) -> int:
    return min(args)


print(get_min_value(a, b, c))