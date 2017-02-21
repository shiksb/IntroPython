def is_anagram(a, b):
    #Your codes here


    return is_an_anagram

if __name__ == '__main__':

    str1 = "Tom Marvolo Riddle"
    str2 = "I am Lord Voldemort"
    str3 = "I am Ansaf your Professor"

    print("Checking for anagrams:", str1, str2)
    print("Your output:", is_anagram(str1,str2))
    print("Expected output:", True)

    print("Checking for anagrams:", str1, str3)
    print("Your output:", is_anagram(str1,str3))
    print("Expected output:", False)
