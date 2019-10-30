from functions import *

# give the user options
print('What do you want to do today?')
print('1 - Check if a number is prime.')
print('2 - find the highest prime in a given range.')
print('Type exit to leave.')

# get the user's input
choice_input = input("Please choose from the above options: ").strip().upper()
# the whole time the user hasn't told us to exit
while choice_input != "EXIT":
    # if they choose to check if a number is prime
    if choice_input == "1":
        # ask them for a number to check is prime
        prime_number_check_input = input("Please input a number that you wish to check is prime: ")
        # if that number is prime
        if is_prime_number(prime_number_check_input):
            # Tell them it's prime
            print('That number is prime!')
            print(" ")
        # if it's not prime
        else:
            # tell them
            print('That number is not prime...')
            print(" ")
    # if the user chooses to check highest prime in a range
    elif choice_input == "2":
        # ask them for the number to check
        print("I, Computebot, will find the highest number up to an including the number you input.")
        prime_number_range_input = input("Please enter the maximum number you wish to find the highest prime for: ")
        # tell the user the highest prime number in that range
        print("The highest prime in the range 0 to {} is: {}.".format(prime_number_range_input, highest_prime_in_range(prime_number_range_input)))
    # if they haven't selected a valid option, tell them
    else:
        print("Sorry, that's not an option! Please try again.")

    # give them the options again
    print('What do you want to do today?')
    print('1 - Check if a number is prime.')
    print('2 - find the highest prime in a given range.')
    print('Type exit to leave.')
    # ask them the options again, so the loop can start again
    choice_input = input("Please choose from the above options: ").strip().upper()