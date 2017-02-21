def cross_sort(L):
    """
    Write a python function crossSort that takes an unsorted list of integers L and returns a new list that fulfills the following requirements:
    - Even-indexed elements (index 0,2,4…) are sorted in ascending order
    - Odd-indexed elements (index 1,3,5…) are sorted in descending order

    Note that the input list L should NOT be changed.

    @type L: list
    @param L: A list of integers

    @rtype: list
    @return: A new list named sorted_list that fulfills the above requirements

    """
    # write your code here

    # collect every other element, sort appropriately
    even_sorted = sorted(L[::2])
    odd_sorted = sorted(L[1::2])
    odd_sorted.reverse()
    sorted_list = []

    for i in range(len(L)):
        # take turns adding items from evens sorted and odds sorted to the
        # new sorted_list array
        if i % 2 == 0:
            sorted_list.append(even_sorted[i//2])
        else:
            sorted_list.append(odd_sorted[i//2])

    return sorted_list



if __name__ == "__main__":
    test_list_1=[1,2,3,4,5]
    print("Input:", test_list_1)
    print("Your output:", cross_sort(test_list_1))
    print("Expected:", [1,4,3,2,5])

    test_list_2=[1,5,9,-2,3,7,100]
    print("Input:", test_list_2)
    print("Your output:", cross_sort(test_list_2))
    print("Expected:", [1,7,3,5,9,-2,100])
