def make_histogram(a):
    #Your codes here
    bins = []
    for i in range(11):bins.append(0)
    for element in a:
        bins[element//10] += 1
    histogram = "\n"
    histogram.lstrip()
    
    for i in range(10):
        if(bins[i] == 0):
            histogram += '{:02d}-{:02d}:\n'.format(10*i,10*i+9)
        else:
            histogram += '{:02d}-{:02d}: {}\n'.format(10*i,10*i+9,bins[i]*'*')
    if(bins[-1] == 0):            
        histogram += '100:\n'
    else:
        histogram += '100:   {}\n'.format(bins[-1]*'*')
    #print (histogram)
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
