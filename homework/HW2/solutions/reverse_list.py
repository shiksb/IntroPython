def reverse_list(L):
    """
    Reverses a list of items

    @type L: list
    @param L: A list of anything: could be strings, ints, floats, booleans

    @rtype: list
    @return: A new list composed of the elements of L in reverse order
    """

    # append items to the new list starting from the end of the original list
    reversed_list = []
    for i in range(len(L)-1, -1, -1):
        reversed_list.append(L[i])

    return reversed_list

if __name__ == '__main__':
    not_reversed_list = [1,2,3,5,7,8]
    print("Input:", not_reversed_list)
    print("Your result:", reverse_list(not_reversed_list))
    print("Expected result:", [8,7,5,3,2,1])

    not_reversed_list = ['i', 'love', '1006', 'more', 'than', 'anyone']
    print("Input:", not_reversed_list)
    print("Your result:", reverse_list(not_reversed_list))
    print("Expected result:", ["anyone","than","more","1006","love","i"])
