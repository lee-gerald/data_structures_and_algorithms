
# pythonic way
def palindrome(s):
    if s == s[::-1]:
        return True
    
    return False


# non pythonic way
def is_palindrome(s):
    original_string = s
    reversed_string = reverse_list(s)

    if original_string == reversed_string:
        return True
    return False

def reverse_list(data):
    data = list(data)
    start_index = 0
    end_index = len(data) - 1

    while end_index > start_index:
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index += 1
        end_index -= 1
        
    # transform list of letters into a string    
    return ''.join(data)

print(is_palindrome('racecar'))
