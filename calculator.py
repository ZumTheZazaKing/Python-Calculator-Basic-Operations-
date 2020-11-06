import math
import time

def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y

def main():

    print("Choices:")
    time.sleep(1)
    print("1. Addition")
    time.sleep(0.25)
    print("2. Subtraction")
    time.sleep(0.25)
    print("3. Multiplication")
    time.sleep(0.25)
    print("4. Division")
    time.sleep(0.25)
    print("5. Exit\n")

    time.sleep(0.5)

    choice = int(input("Pick a choice number(1/2/3/4/5):"))

    time.sleep(0.5)

    if 1 <= choice <=4:
	    print("Enter two numbers you would like to use:\n")

	    num1 = int(input("Number 1:"))
	    num2 = int(input("Number 2:"))
	    txt = "\nThe answer is {}.\n"

	    if choice == 1:
	  	    result = add(num1, num2)
	  	    time.sleep(1)
	  	    print(txt.format(result))
	  	    time.sleep(1.5)

	    elif choice == 2:
	  	    result = subtract(num1, num2)
	  	    time.sleep(1)
	  	    print(txt.format(result))
	  	    time.sleep(1.5)

	    elif choice == 3:
	    	result = multiply(num1, num2)
	    	time.sleep(1)
	    	print(txt.format(result))
	    	time.sleep(1.5)

	    else:
	    	result = divide(num1, num2)
	    	time.sleep(1)
	    	print(txt.format(result))
	    	time.sleep(1.5)

    elif choice == 5:
	    print("\nGoodbye!\n")
	    time.sleep(2)
	    exit()

    else:
	    print("That's the wrong number!")

#The real thing

print("\n-----------------------------------------------------------------")
print("             Welcome To Muhammad Zahidi's Calculator!              ")
print("-----------------------------------------------------------------\n")

while True:

	time.sleep(2)

	main()



