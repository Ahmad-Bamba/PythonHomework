# Book Sales
# Ahmad Bamba
# 09/20/2016

# print "[Debug] I am working"

class Book:
    def __init__(self, t, a, c, r):
        self.title = t
        self.author = a
        self.cost = c
        self.revenue = r

books = [ Book("Apprentice in Death", "J. D. Robb", 17.19, 1727595.0),
          Book("Razor Girl", "Carl Hiaasen", 17.02, 1706255.0),
          Book("The Underground Railroad", "Colson Whitehead", 21.56, 2156000.0),
          Book("A Great Reckoning", "Louise Penny", 17.56, 1751610.0),
          Book("The Woman in Cabin 10", "Ruth Ware", 15.66, 1558170.0),
          Book("Rushing Waters", "Danielle Steel", 17.46, 1732905.0,),
          Book("Here I Am", "Jonathan Safran Foer", 17.13, 1631350.0),
          Book("A Gentleman in Moscow", "Amor Towles", 16.52, 1631870.0),
          Book("Truly Madly Guilty", "Liane Moriarty", 16.51, 1626235.0),
          Book("Downfall", "J. A. Jance", 21.67, 2129077.5) ]

def sortBooks():
    global books # this is needed for some reason

    while True: # run forever until all items are sorted correctly
        # print "[Debug] working..."
        for x in range(len(books) - 1):
            if books[x].cost > books[x + 1].cost:
                # print "[Debug] sorting..."
                # if the earlier entry is larger than the later entry, swap the two objects
                temp = books[x]
                books[x] = books[x + 1]
                books[x + 1] = temp

        # now check to see if we have to run the above loop again
        done = True
        for y in range(len(books) - 1):
            if books[y].cost > books[y + 1].cost:
                # we have to do this again
                # print "[Debug] not done"
                done = False

        if done:
            break


def averageCosts():
    sum = 0
    for book in books:
        sum += book.cost

    return sum / len(books)

def getMostExpensive():
    return books[len(books) - 1]

def getLeastExpensive():
    return books[0]

def printBooks(b):
    print "Title: " + b.title + " Author: " + b.author + " Cost: $" + str(format(b.cost, ".2f")) + " Gross Revenue: $" + str(format(b.revenue, '.2f'))

def solution():
    global books
    
    sortBooks()
    print "Here are the books sorted by cost: "
    for book in books:
        printBooks(book)

    print "The average cost is: $" + str(format(averageCosts(), ".2f"))
    print "The most expensive book is: " + getMostExpensive().title
    print "The least most expensive book is: " + getLeastExpensive().title

    print "Now we will add 'Harry Potter and the Half Blood Prince' by J.K. Rowling"
    books.append(Book("Harry Potter and the Half Blood Prince", "J.K. Rowling", 18.29, 16866000))
    print "Resorting list..."
    sortBooks()
    print "Here are the books sorted by cost: "
    for book in books:
        printBooks(book)

    print "The new average cost per book is: $" + str(format(averageCosts(), ".2f"))
    

solution()
