def is_permutation(L):
    n = len(L)
    # makes sure that exactly each of the integers in the expected range
    # are present
    integer_dict = {x: False for x in range(1, n+1)}
    for integer in L:
        # only includes integers in the correct range, which are all the keys
        # of this dictionary
        if integer in integer_dict:
            integer_dict[integer] = True
    # checks if any of the integers between 1 and n were missing
    # if they are all present, then there can be no extras, because the range
    # of values is tied directly to the size of the list
    is_a_permutation = True
    for integer in integer_dict:
        # if any of the values are missing, then it is not a permutation
        if integer_dict[integer] == False:
            is_a_permutation = False
            break

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
