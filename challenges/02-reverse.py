# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1
# 
### MY WAY ### 
# user_string = input('Enter a string to be reversed: ')
# print(f'Reversing: {user_string}...')
# reversed_string=[]
# i = len(user_string)
# while i > 0:
#     reversed_string.append(user_string[i - 1])
#     i -= 1
# print(''.join(reversed_string))

should_run = True
while should_run:
    print("Enter a string to be reversed! (enter q to quit)")

    string = input('>')
    
    if string == 'q':
        should_run = False

    new_string = ''

    for char in string:
        new_string = char + new_string

    print(new_string)