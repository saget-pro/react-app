def print_numbers(n, limit):
    if n > limit:
        return
    print(n)
    print_numbers(n + 1, limit)

print_numbers(1, 10000000)
