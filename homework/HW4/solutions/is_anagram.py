def buildLetterCountDict(sentence):
    counts = {}
    lower_s = sentence.lower()
    for letter in lower_s:
        if letter.isalpha():
            if letter not in counts:
                counts[letter] = 1
            else:
                counts[letter] += 1
    return counts

def is_anagram(a, b):
    a_counts = buildLetterCountDict(a)
    b_counts = buildLetterCountDict(b)
    is_an_anagram = a_counts == b_counts
    return is_an_anagram

if __name__ == '__main__':

    str1 = "Tom Marvolo Riddle"
    str2 = "I am Lord Voldemort"
    str3 = "I am Ansaf your Professor"

    print("Checking for anagrams:", str1, '||', str2)
    print("Your output:", is_anagram(str1,str2))
    print("Expected output:", True)

    print("Checking for anagrams:", str1, '||', str3)
    print("Your output:", is_anagram(str1,str3))
    print("Expected output:", False)
