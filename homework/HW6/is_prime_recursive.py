def is_prime_recursive_driver(n, i):
    # no need to make i any higher at this point, have not found any factors
    # yet so we never will, making it prime
    if i ** 2 > n:
        return True
    # divisible by some number so can't be prime
    if n % i == 0:
        return False
    else:
        # try a higher possible factor
        return is_prime_recursive_driver(n, i+1)

def is_prime_recursive(n):
    # definition
    if n < 2:
        return False
    else:
        return is_prime_recursive_driver(n, 2)

if __name__ == "__main__":
    testcases = [-1, 0, 1, 2, 3, 5, 18, 25]
    for test in testcases:
        is_prime = is_prime_recursive(test)
        is_prime_str = "" if is_prime else " not"
        print("%d is%s prime" % (test, is_prime_str))
