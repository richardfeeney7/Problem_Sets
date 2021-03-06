#                                    Author Richard Feeney
#                                       Date 22/02/2017

#                                        Problem 4 : 
 
'''    Write a program that asks the user to input any positive integer and outputs the successive values 
       of the following calculation. At each step calculate the next value by taking the current value and,
       if it is even,divide it by two,but if it is odd,multiply it by three and add one.
'''

def user_input(num):        # Define function
    print(num)              # Print num
    while num > 1:          # This will check user input and loops while > 1. If i had > 0 is would run an infinite loop with the number 1
        if num % 2 == 0:    # Checks the remainder of num and if = 0 continue
            num = num/2     # Divide num by 2 
            print(int(num)) # Print the output. INT was declared because it was outputting a Float

        else:                 # Will be used if the number is an odd number 
            num = (num*3) + 1 # If number is odd this calculation will be stored and printed to the screen
            print(int(num))   # Print the output. INT was declared because it was outputting a Float

    if num < 1:                     # Check is num < 1 and prints try again
        print("Please try again")   # Prints output

user_input(int(input("Please enter a positive number : "))) #Store user input in user_input