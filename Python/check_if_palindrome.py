def check_if_palindrome():
    str = raw_input("Enter a string: ")
    reverse = str[::-1]
    if str == reverse:
        print("{} is a palindrome".format(str))
    else:
        print("{} is not a palindrome".format(str))


check_if_palindrome()