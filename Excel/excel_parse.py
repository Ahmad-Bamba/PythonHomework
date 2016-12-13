# Excel to CSV File Practice
# Ahmad Bamba
# 12/09/2016

# This code assumes the days of Christmas are listed in order.
# I have no idea why this works but it does so I'm not gonna touch it

import sys

class Day:
    def __init__(self, row):
        self.number = row[0]
        self.gift = row[1]
        self.price = row[2]

    def getNumber(self):
        return self.number
    def getGift(self):
        return self.gift
    def getPrice(self):
        return self.price

_file = open("04 - 12 Days of Christmas Gifts.csv")
raw = _file.read()
_file.close()

lines = raw.splitlines()
formatted = [line.split(",") for line in lines]
print formatted
days = []

for thing in formatted:
    days.append(Day(thing))

def calc(num):
    total = 0.00
    for i in xrange(num):
        day = days[i]
        total += float(day.getPrice()) * float(day.getNumber())
        print "\t" + str(day.getNumber()) + " : " + str(day.getGift()) + " : " + str(day.getPrice())
    return total

while True:
    user = raw_input("\nEnter day of Christmas(q to quit): ")
    if user.lower() == "q":
        "Exiting on user request"
        sys.exit()
    if int(user.lower()) not in xrange(1, 12):
        print "Not a valid day number"
    else:
        print "The gifts for day " + str(user.lower()) + " are:"
        print "Price of day " + user + " : "  + "$" + "{0:.2f}".format(calc(int(user)))
        total = 0.00
        for i in xrange(int(user)):
            print calc(i + 1)
            total += calc(i + 1)
        print "Price of all the days: " + "$" + "{0:.2f}".format(total)
