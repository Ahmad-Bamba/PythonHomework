# ISBN Validator
# Ahmad Bamba
# 10/28/2016

def isNumber(digit):
    try:
        int(digit)
        return True
    except Exception as e:
        return False
        
def doFormat(isbn):
    new = []
    for i in xrange(len(isbn)):
        if (not (isbn[i] == "-")) and (isNumber(isbn[i]) or isbn[i].upper() == "X"):
            # print "Appending " + isbn[i]
            new.append(isbn[i])
    return new

def validate(isbn):
    if not (len(isbn) == 10):
        print "Invalidated by length!"
        return False

    total = 0
    for i in xrange(len(isbn)):
        if isbn[i].upper() == "X":
            total += 10 * (10 - i)
        else:
            total += int(isbn[i]) * (10 - i)
    if total % 11 == 0:
        return True
    return False

def getInput():
    isValid = validate(doFormat(str(raw_input("Enter ISBN: "))))
    if isValid:
        print "This is a valid ISBN number!"
    else:
        print "Invalid ISBN number!"

getInput()
