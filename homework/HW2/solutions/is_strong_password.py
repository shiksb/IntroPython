def satisfies_length_req(s):
    n = len(s)
    return n >= 6 and n <= 20

def at_least_one_of_each_req(s):
    lowers = 'abcdefghijklmnopqrstuvwxyz'
    uppers = lowers.upper()
    nums = '0123456789'
    hasLowers = False
    hasUppers = False
    hasNums = False
    for char in s:
        if char in lowers:
            hasLowers = True
        elif char in uppers:
            hasUppers = True
        elif char in nums:
            hasNums = True

    return hasLowers and hasUppers and hasNums

def contains_repeated_char(password):
    for i in range(2, len(password)):
        if password[i-2] == password[i-1] == password[i]:
            return True
    return False

def is_strong_password(password):
    '''
    A password is considered strong if all the following requirements are met:
    The password must be at least 6 characters and at most 20 characters
    It must contain at least one lowercase letter, at least one uppercase letter, and at least one number
    It must NOT contain a character that is repeated consecutively more than twice at any point. A password that contains “111” anywhere within it would be weak, but a password like “...11….1….11” would be strong, assuming other requirements are met within the “...”

    Write a function that takes a string argument “password” and checks if “password” meets all of the strong requirements. If it does, return True. Otherwise, return False.
    @type password: string
    @param password: a string whose password strength will be checked

    @rtype bool
    @return True if password is strong, otherwise False
    '''
    if not satisfies_length_req(password) or not at_least_one_of_each_req(password) \
        or contains_repeated_char(password):
        return False
    else:
        return True

if __name__ == "__main__":
    pass1 = "1a9fj"
    print("Input:", pass1)
    print("Your output", is_strong_password(pass1))
    print("Expected output", False)

    pass2 = "js88Sjf99"
    print("Input:", pass2)
    print("Your output", is_strong_password(pass2))
    print("Expected output", True)

    pass3 = "ys9aS890sFFFFn"
    print("Input:", pass3)
    print("Your output", is_strong_password(pass3))
    print("Expected output", False)
