from functions import *

print('What do you want to do today?')
print('1 - Check if a number is prime.')
print('2 - find the highest prime in a given range.')
print('Type exit to leave.')

choice_input = input("Please choose from the above options: ").strip().upper()
while choice_input != "EXIT":
    if choice_input == "1":
        prime_number_check_input = input("Please input a number that you wish to check is prime: ")
        if is_prime_number(prime_number_check_input):
            print('That number is prime!')
            print(" ")
        else:
            print('That number is not prime...')
            print(" ")
    elif choice_input == "2":
        print("I, Computebot, will find the highest number up to an including the number you input.")
        prime_number_range_input = input("Please enter the maximum number you wish to find the highest prime for: ")
        print("The highest prime in the range 0 to {} is: {}.".format(prime_number_range_input, highest_prime_in_range(prime_number_range_input)))
    else:
        print("Sorry, that's not an option! Please try again.")

    print('What do you want to do today?')
    print('1 - Check if a number is prime.')
    print('2 - find the highest prime in a given range.')
    print('Type exit to leave.')
    choice_input = input("Please choose from the above options: ").strip().upper()



# print(is_prime_number(15))

# print(highest_prime_in_range(8))

# user_input_prime = input('Please input a number for the range of which you\'d like to find prime numbers for: ')

# all_primes_in_range(user_input_prime)