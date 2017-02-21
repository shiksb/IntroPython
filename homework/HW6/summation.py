def summation(n):
    if n <= 0:
        return 0
    else:
        return n**3 + summation(n-1)

if __name__ == "__main__":
    testcases = [1, 4, 9]
    for test in testcases:
        print("Summation of %d is %d" % (test, summation(test)))
