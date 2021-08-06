word_1 = "bonsor"
word_2 = "robson"
# is_anagram=[]

# def anagram(string_1, string_2):
#     for x in string_1:
#         for y in string_2:
#             if x == y:
#                 is_anagram.append(x)
#                 if len(is_anagram) == len(string_1) or len(is_anagram) == len(string_2):
#                     print("anagram!")
#                     return is_anagram

# print(anagram(word_1, word_2))


############ INSTRUCTOR SOLUTION ##########
str1 = ['r','e','s','t','f','u','l']
str2 = ['f','l','u','s','t','e','r']

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    
    return True

print(is_anagram(word_1, word_2))
