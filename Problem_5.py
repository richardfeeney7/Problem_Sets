#                              Author : Richard Feeney 
#                               Started: 25/02/2019

#                                    Problem 5 :    
# Write a program that asks the user to input a positive integer and tells the user whether or not the number 
#                                     is a prime.       



# If statement in comments below didn't give me the desired output. I needed to insert a range function.
'''
y=2
if num > 1:
    if num % y == 0:
        print("Your number ",num, " is NOT a prime") 
    else:
        print("Your number ",num, " is a prime")
'''

def prime(num):                 # Define the function

# Used assert to output a message when the num entered is >=1. Previously I had used the IF ELSE method. 
    assert num >=2, "Number cant be negative and must be greater than 1"

    # When 2 was entered in the for loop it was not outputting as 2 is the only even prime number. 
    if num == 2:
            print(f"Success {name}, ", num, "is a prime number" )

   # if num > 1:            # Start IF statement to search for prime number. Not used after Assert addition
    for i in range(2,num):  # Create the range function starting at 2 that also accepts the user input paramater
        if num % i == 0:    # Check if user input % 1 = 0, if true continue.
            #print("Sorry" ,name, num, "is not prime")
            print(f"Sorry {name}," ,num, "is not prime") # Modified above print to use formatted string
            break   # Break out of statement

        else:
            # print("Yes", name, num, "is a prime number") 
            print(f"Success {name},",num,"is a prime number") # Modified above print to use formatted string
            break   # Break out of statement

'''
    elif num == 1:              # 1 cant be a prime number as it only has 1 factor
        print("Sorry", num, "is not a prime number")  

    elif num < 0:               # A prime number cant be a negative number
        print("A prime number cant be a negative number")
'''

name = input("Hello and welcome to my application, please input your name ? ")
prime(int(input("Please enter a positive number : "))) # Accepts the user number and sends to function