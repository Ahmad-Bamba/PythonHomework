# Alphabetical Order
# Ahmad Bamba
# 10/26/2016

def isTripleConsecutive(w):
    word = w.upper()
    if(len(word) < 3):
        return False
    if(len(word) == 3):
        if (ord(word[1]) == ord(word[0]) + 1) and (ord(word[2]) == ord(word[1]) + 1):
            return True
    for i in xrange(len(word) - 3):
        print word[i]
        if (ord(word[i + 1]) == ord(word[i]) + 1) and (ord(word[i + 2]) == ord(word[i + 1]) + 1):
            return True
    return False

def getInput():
    print "Does your word contain a triple consecutive?: " + str(isTripleConsecutive(str(raw_input("Enter word: ")))) # fun

getInput()
