# Palindrome
# Ahmad Bamba
# 09/30/2016

def strip(phrase):
    val = ""
    no = "-,./;:&' "

    temp = phrase.lower()

    for char in temp:
        if(char not in no):
            val += char

    return val

def reverse(phrase):
    return phrase[::-1]

def out():
    while True:
        user = str(raw_input("Insert phrase (-1 to quit): "))
        if user == "-1":
            break

        if reverse(strip(user)) == strip(user):
            print "This phrase is a palendrome"
        else:
            print "This phrase is not a palendrome"

out()
