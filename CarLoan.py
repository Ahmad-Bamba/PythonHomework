# Car Loan
# Ahmad Bamba
# 9/14/2016

def calc(i, a, n):
    return (i/(1 - ((1+i) ** (-12 * n)))) * a

def findi(r):
    return r/1200

def prompt():
    rate = float(raw_input("What is the r% interest?: ")) # creates divide by zero error if r is not a decimal
    loan = int(raw_input("How much money is being borrowed?: "))
    time = int(raw_input("How many years will you take to pay off the loan?: "))

    # Use findi() to find i, use calc() to find monthly interest, use round to
    # round to 2 decimal places, and use format to force 2 decimal places even
    # if the answer only has one decimal place

    print "Your monthly payment is: $" + str(format(round(calc(findi(rate), loan, time), 2), '.2f'))

prompt()
