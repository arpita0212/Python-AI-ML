def is_palindrome(s):
    originalVal = "madam"
    reverseVal = s[::-1]

    if originalVal == reverseVal:
        return True
    else:
        return False


print(is_palindrome("madam"))