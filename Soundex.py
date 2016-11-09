# Soundex
# Ahmad Bamba
# 09/22/2016

def soundex(word):
    answer = []
    w = []

    for letter in word:
        w.append(letter)
        
    for i in range(len(w) - 2):
        if w[i] == "a" or w[i] == "e" or w[i] == "i" or w[i] == "o" or w[i] == "u" or w[i] == "h" or w[i] == "y" or w[i] == "w":
            w[i] = " "

    answer.append(w[0])
    for letter in w:
        if letter == "b" or letter == "f" or letter == "p" or letter == "v":
            answer.append("1")
        elif letter == "c" or letter == "g" or letter == "j" or letter == "k" or letter == "q" or letter == "s" or letter == "x" or letter == "z":
            answer.append("2")
        elif letter == "d" or letter == "t":
            answer.append("3")
        elif letter == "l":
            answer.append("4")
        elif letter == "m" or letter == "n":
            answer.append("5")
        elif letter == "r":
            answer.append("6")

    answer2 = []

    for letter in answer:
        if letter not in answer2:
            answer2.append(letter)

    if len(answer2) >= 4:
        returnval = str(answer2[0] + answer2[1] + answer2[2] + answer2[3])
        print "5 " + str(returnval)
        return returnval
    else:
        returnval = ""

        for char in answer2:
            returnval += char

        for i in range(4):
            returnval += "0"
        
        return returnval[:4]

def out():
    while True:
        user = str(raw_input("Enter Word (:q for exit): "))
        if user == ":q":
            break

        print "Your soundex formatted word is: " + "".join(soundex(user)) + "\n"

out()
