# # # wap to takeke a string input from the user and print in rev.
# # # number ofo uppercase and lower case in a String 
# # check whether a given string contain only digits
# # replace all space in string with underscore
# # count the frequency of each cahracter in a string
# first and last occurance of a character in a String
s = input("Enter a string: ")

upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
#------------------------------------------------------------------------------
s = input("Enter a string: ")

if s.isdigit():
    print("The string contains only digits")
else:
    print("The string does not contain only digits")
#
