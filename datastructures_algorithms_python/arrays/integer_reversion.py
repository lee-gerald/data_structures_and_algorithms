# my solution

# int = 1234

# def reverse_integer(int):
#     data = str(int).split()
#     start_index = 0
#     end_index = len(data)-1
#     temp = 0

#     while end_index > start_index:
#         temp = data[start_index]
#         data[end_index] = data[start_index]
#         data[start_index] = temp
#     return int(data)


# print(reverse_integer(int))
################FAILED####################

# instructor solution
def instructor_reverse_integer(n):
    reversed_integer = 0

    while n > 0:
        remainder = n % 10
        reversed_integer = reversed_integer * 10 + remainder
        n = n // 10 # integer division

    return reversed_integer


print(instructor_reverse_integer(1234))