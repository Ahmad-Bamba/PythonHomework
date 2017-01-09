# Sports Ball Prizes
# Ahmad Bamba
# 11/29/2016

# Non ascii spaces and other characters were removed for this to work

import string
printable = set(string.printable)

lines = []
clean = []
teams = set() # contains all unique teams
pairs = []

for line in open("Rosebowl.txt", 'r'):
    lines.append(filter(lambda x: x in printable, line)) # use only printable characters

for line in lines:
    clean.append(line.replace("\n", ""))

for i in xrange(len(clean)):
    clean[i] = clean[i][5:].strip() # remove the year and first space and remove whitespace

teams = set(clean)

for team in teams:
    pairs.append((team, clean.count(team)))

sorted_list = sorted(pairs, key = lambda x: int(x[1]), reverse = True)

for team in sorted_list:
    if team[1] >= 4:
        print "Team " + team[0] + " has one " + str(team[1]) + " times!"
