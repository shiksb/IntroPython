def missing_letters(s):
    """
    @type s: str
    @param s: String

    @rtype: List
    @return: Returns a list of the letters not present in the string
    """

    # Write your code below.

    # every index in this list represents the index of a letter in the alphabet
    s = s.lower()
    letter_present = [False for i in range(26)]

    for letter in s:
        # use ASCII to find out the index of the current letter in the alphabet
        if letter.isalpha():
            index = ord(letter) - ord('a')

            # mark that letter as being seen
            letter_present[index] = True

    result = []
    for idx in range(len(letter_present)):
        if not letter_present[idx]:
            # convert back to letter
            missing_letter = chr(idx + ord('a'))
            result.append(missing_letter)

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
