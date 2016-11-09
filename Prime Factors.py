# Prime Factors
# Ahmad Bamba
# 10/18/2016

import sys

def sanitize(number):
    if int(number) > 1:
        return int(number)
    else:
        return -1

def getFactors(number):
    factors = [1, number]
    for i in xrange(2, number):
        if number % i == 0:
            factors.append(i)
    return factors

def getPrimes(numbers):
    useThis = numbers
    primeNumbers = []

    for number in numbers:
        if number == 2:
            primeNumbers.append(2)

    # remove all the 2s in the list, as they have been taken care of
    filter(lambda a: a != 2, useThis)

    for number in useThis:
        isPrime = True
        for i in xrange(2, number):
            if number % i == 0:
                isPrime = False
        if (isPrime):
            primeNumbers.append(number)

    return primeNumbers

def getSpecialFactors(primefactors):
    pf = primefactors
    pf.sort()

    # Start at index 1 because 1 is in index 0
    # This is totally valid, shut up Champ
    if(len(pf) <= 2):
        return ("None", pf[1])
    return (pf[1], pf[len(pf) - 1])

def getInput():
    try:
        user = int(raw_input("Enter number: "))
    except Exception as e:
        print "Not a number!"
        sys.exit()

    user = sanitize(user)
    if user < 0:
        print "Number must be positive!"
        sys.exit()

    user_factors = getFactors(user)
    user_prime_factors = getPrimes(user_factors)
    answer = getSpecialFactors(user_prime_factors)

    print "The largest prime is: " + str(answer[1])
    print "The smallest prime is: " + str(answer[0])


getInput()
