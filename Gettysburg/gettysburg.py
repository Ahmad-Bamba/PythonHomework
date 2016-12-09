# Gettysburg Address
# Ahmad Bamba
# 11/17/2016

from sets import Set
import re

f = open("Gettysburg.txt", 'r')
string = f.readline()
string.replace("-", "") # Hyphens mess up re.sub()
f.close()

print string[:88]
wordList = re.sub("[^\w]", " ",  string).split()
print str(len(wordList)) + " words found."
words = Set([])

for word in wordList:
    words.add(word.lower())
    
print "Found " + str(len(words)) + " unique words"
