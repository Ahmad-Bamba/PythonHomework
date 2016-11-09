# Bond Yield
# Ahmad Bamba
# 9/14/2016

def prompt():
    # gather information needed
    face = float(raw_input("What was the face value of the bond?: "))
    current = float(raw_input("What is the current price of the bond?: "))
    time = float(raw_input("Time until maturity?: "))
    interest = intr(float(raw_input("What is the interest rate percent?: ")))

    # math
    solution = (YTM(interest, a(face, current, time), b(face, current))) * 100

    #present result
    print "The estimated YTM of the bond is " + str(format(solution, '.2f')) + "%"
    

def a(f, c, t):
    return (f - c) / t

def b(f, c):
    return (f + c) / 2

def intr(x):
    return (x/100) * 1000 # it says to do this on the assigment but idk why

def YTM(i, a, b):
    return (i + a) / b

prompt()
