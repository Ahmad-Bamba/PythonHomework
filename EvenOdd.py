# Even Odd program
# Ahmad Bamba
# 9/12/2016

def evenodd(x):
    if (x % 2) == 0:
        print "The number is even"
    else:
        print "The number is odd"

evenodd(int(input("Enter number: ")))

closeInput = input("Press ENTER to exit")
print "Exiting..."
