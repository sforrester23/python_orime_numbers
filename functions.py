# function for determining if the argument parsed number is prime or not
def is_prime_number(number):
    # make it an integer
    number = int(number)
    # start the count
    index = 1
    # make an empty list of the number's factors
    list_of_factors = []
    # for the whole time the count is below or equal to the number
    while index <= number:
        # if the number is divisible by the count
        if number%index == 0:
            # add that number to the factors list, as it is a factor of the number
            list_of_factors.append(index)
        # count up, regardless of whether it is a factor or not (hence the indent)
        index += 1

    # if the list of factors is only 1 and the number itself, it is by definition, prime!
    if list_of_factors == [1, number]:
        return True
    else:
        return False

# function for finding the highest number in a range (assuming range starts at zero, only taking an argument of the highest number)
def highest_prime_in_range(number):
    # make sure the argument number is an integer
    number = int(number)
    # the highest prime to begin with is, by default, 1
    highest_prime = 1
    # iterate over the range of values 0 to the inputted number (using index placeholder, so we need the highest to be number+1 as they count from 0, not 1)
    for index in range(1, number+1):
        # if the number is prime, set the highest prime so far to be that
        if is_prime_number(index):
            highest_prime = index
        # by the end of the loop, we have checked all numbers, and therefore the highest_prime variable will hold the highest prime
    # return it
    return highest_prime

