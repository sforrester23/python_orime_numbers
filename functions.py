def is_prime_number(number):
    number = int(number)
    index = 1
    list_of_factors = []
    while index <= number:
        if number%index == 0:
            list_of_factors.append(index)
        index += 1


    if list_of_factors == [1, number]:
        return True
    else:
        return False

def highest_prime_in_range(number):
    number = int(number)
    highest_prime = 1
    for index in range(1, number+1):
        if is_prime_number(index) == True:
            highest_prime = index
    return highest_prime

