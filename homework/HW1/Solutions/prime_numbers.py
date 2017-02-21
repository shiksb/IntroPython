num = int(input("Check the primality of this number: "))
i = 2
# anything less than or equal to 1 is not prime
isPrime = True if num > 1 else False
# stop when i has exceeded sqrt(num) (since there could be no factors higher
# than sqrt(num) that wouldn't have a corresponding factor below sqrt(num)

while (i ** 2 <= num):
    if num % i == 0:
        isPrime = False
        # immediately break upon seeing the first factor, since all it takes is
        # one factor besides 1 and itself for a number to not be prime
        break
    i += 1

if isPrime:
    print(num, "is prime")
else:
    print(num, "is not prime")
