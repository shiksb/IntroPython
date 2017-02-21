def is_permutation(L):
    #Your codes here


    return is_a_permutation


if __name__ == '__main__':

    test_1 = [1,2,3,4,5]
    test_2 = [1,3,2,5,4]
    test_3 = [1,2,3,-5,8,0]
    test_4 = [1,1,2,3,4,5]

    print("Test 1 Input:", test_1)
    print("Your output:", is_permutation(test_1))
    print("Expected output:", True)

    print("Test 2 Input:", test_2)
    print("Your output:", is_permutation(test_2))
    print("Expected output:", True)

    print("Test 3 Input:", test_3)
    print("Your output:", is_permutation(test_3))
    print("Expected output:", False)

    print("Test 4 Input:", test_4)
    print("Your output:", is_permutation(test_4))
    print("Expected output:", False)
