num = int(input("Check if this number is perfect: "))
i = 1
# initialize to -num since we're always adding both factors, which would
# include 1 and num itself
factorSum = -num
# increase until i has exceeded the sqrt of n
while (i ** 2 <= num):
    # check divisibility
    if num % i == 0:
        # add both factors simultaneously
        factorSum += (num / i + i)
    if i ** 2 == num:
    	factorSum -= i
    i += 1
if num == factorSum:
    print(True)
else:
    print(False)
