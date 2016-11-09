# Numbers
# Ahmad Bamba
# 11/09/2016

def isNumber(var):
    try:
        int(var)
        return True
    except Exception as e:
        return False

def getList(filename):
    numbers = []
    f = open(filename, 'r')
    filestring = f.read()
    for char in filestring:
        if isNumber(char):
            numbers.append(int(char))
    f.close()
    return numbers

def getInput():
    user = str(raw_input("File name?: "))
    print "The number of numbers in this file is: " + str(len(getList(user)))
    print "The maximum value of the numbers list is: " + str(max(getList(user)))
    print "The minimum value of the numbers list is: " + str(min(getList(user)))
    print "The numerical sum is: " + str(sum(getList(user)))
    print "The mean is: " + str(sum(getList(user))/len(getList(user)))

getInput()
