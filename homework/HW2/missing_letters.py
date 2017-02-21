def missing_letters(s):
    """
    @type s: str
    @param s: String

    @rtype: List
    @return: Returns a list of the letters not present in the string
    """

    # Write your code below.

    return result

if __name__ == "__main__":
    test_string_1="The quick brown fox jumps over the lazy dog"
    print("Input:", test_string_1)
    print("Your output:", missing_letters(test_string_1))
    print("Expected:", [])

    test_string_2="The brown fox jumps over the dog"
    print("Input:", test_string_2)
    print("Your output:", missing_letters(test_string_2))
    print("Expected:", ['a','c','i','k','l','q','y','z'])
