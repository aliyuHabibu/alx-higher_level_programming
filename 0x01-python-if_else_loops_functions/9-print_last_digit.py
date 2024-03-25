def print_last_digit(number):
    i = number % 10
    if i < 0:
        i = -1 * i
        print(f"{i}", end='')
        return i
    else:
        print(f"{i}", end='')
        return i
