def get_digit(digit, lenght):
    for i in range(lenght-1):
        digit //= 10
    return digit % 10


def get_num_difit(digit):
    i = 0
    while digit > 0:
        digit //= 10
        i += 1
    return i


def radix_sort(array, max_value):
    """Radix sort sorts each digit from least significant digit to most significant digit"""
    num_digits = get_num_difit(max_value)
    for lenght in range(num_digits):
        array = counting_sort(
            array, max_value, lambda a: get_digit(a, lenght+1))
    return array


# VERY MUCH TODO HERE
