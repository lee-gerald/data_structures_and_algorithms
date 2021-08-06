# my solution

word = "aaaa"
def is_palindrome(word):
    start_index = 0
    end_index = len(word)-1

    while end_index >= start_index:
        if start_index == end_index:
            return print("it is a palindrome")
        elif word[start_index] == word[end_index]:
            start_index += 1
            end_index -= 1
        else:
            return print("not a palindrome")

# print(is_palindrome(word))

# instructor solution

# pythonic way
def palindrome_python(s):
    if s == s[::-1]:
        return True
    
    return False

# print(palindrome_python('racecar'))

# non pythonic way
def instructor_is_palindrome(s):
    original_string = s
    reversed_string = instructor_reverse_list(s)

    if original_string == reversed_string:
        return True
    return False

def instructor_reverse_list(data):
    data = list(data)
    start_index = 0
    end_index = len(data) - 1

    while end_index > start_index:
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index += 1
        end_index -= 1
    # transform list of letters into a string    
    return ''.join(data)

print(instructor_is_palindrome('racecar'))
