num = int(input("Convert a non-negative number to binary: "))
res = "" if num != 0 else "0"
while num != 0:
    remainder = num % 2
    num = num // 2
    res = str(remainder) + res
print(res)
