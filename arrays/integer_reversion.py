def reverse_integer(n):
    reversed_integer = 0

    while n > 0:
        remainder = n % 10
        reversed_integer = reversed_integer * 10 + remainder
        n = n // 10

    return reversed_integer


print(reverse_integer(1234))