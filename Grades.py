# Test Grade Program
# Ahmad Bamba
# 9/12/2016

def parselettergrade(grade):
    if grade >= 91:
        return "A"
    elif grade >= 81:
        return "B"
    elif grade >= 71:
        return "C"
    elif grade >= 61:
        return "D"
    else:
        return "F"

score = int(input("What did you get on the test? "))
print ("Your letter grade is: " + parselettergrade(score))

x = input("Press ENTER to close ")
print "Closing..."
