num = input("Please enter an integer or X: ")
total = 0
minNum = float('inf')
maxNum = -float('inf')
while num != "X":
    int_num = int(num)
    if int_num < minNum:
        minNum = int_num
    if int_num > maxNum:
        maxNum = int_num
    total += int_num
    num = input("Please enter an integer or X: ")
print("Sum: %d, Min: %d, Max: %d" % (total, minNum, maxNum))
