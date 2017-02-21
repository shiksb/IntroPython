def make_histogram(a):
    #Your codes here


    return histogram

if __name__ == '__main__':

    input_list = [73, 65, 92, 74, 100, 70]
    expected_result=\
"""
00-09:
10-19:
20-29:
30-39:
40-49:
50-59:
60-69: *
70-79: ***
80-89:
90-99: *
100:   *
"""
    print("Input:", input_list)
    print("Your result:\n", make_histogram(input_list))
    print("Expected result:\n", expected_result)
