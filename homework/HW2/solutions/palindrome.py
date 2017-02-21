"""

"""

def palindrome(s):
    """
    @type s: str
    @param s: A string

    @rtype: int
    @return: Returns the minimum number of characters that need to be replaced
                for s to be a palindrome
    """
    lower_s = s.lower()
    # write your code here
    count = 0
    for i in range(len(lower_s)//2):
        # opposite letters aren't equal, meaning that if one of them is changed
        # to become the other then it would be symmetrical
        if lower_s[i] != lower_s[len(lower_s) - i - 1]:
            count += 1

    return count

if __name__=="__main__":
    s = "abccb"
    print("Your input ", s)
    print("Your output:", palindrome(s))
    print("Expected output:", 2)

    s = "abccbA"
    print("Your input ", s)
    print("Your output:", palindrome(s))
    print("Expected output:", 0)
