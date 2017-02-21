import random

def piri():
	"""
	Calling piri() starts a user-interactive progam with four functionalities:
		1) Give me a random number between X and Y
		2) What is my BMR?
		3) Tell me if this number is prime.
		4) Exit
	Upon selecting "Exit", the program returns and ends.

	@params: None
	"""
	name = input("Hi, I am your personal assistant Piri. What is your name?\n")
	menu = "Hi, " + name + """! What can I do for you? Select from:
		1) Give me a random number between X and Y
		2) What is my BMR?
		3) Tell me if this number is prime.
		4) Exit\n"""
	selection = input(menu)

	while selection != "Exit" and selection != "4":

		if (selection == "1" or
		    selection == "Give me a random number between X and Y"):
			rangeVal = input("Between which numbers would you like me to pick?")
			x,y=rangeVal.split(" ") #parse the input to get two values
			x,y=int(x),int(y) #cast values to integers
			randomVal = bound_random(x,y)
			print (randomVal, "is a random number between", x, "and", y)

		elif (selection=="2" or
			  selection=="What is my BMR?"):

			weight = getNonNegativeVal("What is your weight in pounds?")
			height = getNonNegativeVal("What is your height in inches?")
			age = getNonNegativeVal("What is your age?")
			gender = input('"m" or "f"?')
			while gender!="m" and gender!="f":
				gender = input('"m" or "f"?') #keep asking until valid input
			bmrResult=bmr(weight,height,age,gender)
			#use string formatting to make sure BMR has two decimal places
			print ("Your BMR is %0.2f"%bmrResult)

		elif (selection=="3" or
			  selection=="Tell me if this number is prime."):

			num = float(input("Which number?"))
			if num != int(num):
			    #which means num is a floating point number
			    #note that this is not required after update of question spec
				print (num,"is not prime")
			elif num<=0:
				#negatives -- handle before passing num to prime
				num = int(num)
				print (num,"is not prime")
			else:
				num = int(num)
				if prime(num): # equiv to 'if prime(num)==True'
					print (num,"is prime")
				else:
					print (num,"is not prime")
		else:
			print("I'm sorry, I don't understand.")

		selection = input(menu) #prompt menu again

	print ("Have a good day, " + name + "!")


	return None

def getNonNegativeVal(prompt):
#A helper function that keeps prompting until we get a non-negative input.
#Can be reused several times in piri()
	result = float(input(prompt))
	while result<0:
		result=float(input(prompt))
	return result

def bound_random(x, y):
    """
    @params:
    x: int, lower bound
    y: int, upper bound

    @return: a random int within range [x, y).

    Function assumes x < y.
    """

    n = random.randrange(x,y) #randrange excludes y. different from randint

    return n


def bmr(weight, height, age, gender):
    """
    Computes Basal Metabolic Rate based on English BMR formula.

    @params:
    weight: int, lbs
    height: int, inches
    age: int, years
    gender: str, "m" or "f"

    @return: float BMR truncated to the hundredths.
    """
    if gender == "m":
    	bmr = 66 + ( 6.23 * weight) + ( 12.7 * height) - ( 6.8 * age)
    else:
    	bmr = 655 + ( 4.35 * weight) + ( 4.7 * height)  - ( 4.7 * age)

    return bmr



def prime(x):
	"""
	@params:
	x: int

	@return: True if x is prime, False otherwise.

	Function assumes positive x.
	"""
	isPrime = True

	if x<=1:
		return False

	for i in range(2,int(x**0.5)+1): #go up to sqrt(x) + 1
		if (x % i == 0):
			isPrime = False
			break #break whenever we find one factor
	return isPrime

if __name__ == "__main__":
    piri()
