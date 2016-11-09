# Depreciation
# Ahmad Bamba
# 10/20/2016

# method 0 is SL and method 1 is DDB

def getDep(year, costinit, life, method):
    startvals = []
    yeardep   = []
    total     = []
    constant  = 0
    if method == 1:
        constant = 2.0
    else:
        constant = 1.0
    
    cost = costinit
    now  = year
        
    for x in xrange(life):
        temp = cost
        startvals.append([now, temp])
        print str(cost - ((constant/life) * cost))
        cost = cost - ((constant/life) * cost)
        yeardep.append([year, temp - cost])
        sumc = 0.0
        for y in xrange(len(yeardep)):
            sumc += yeardep[y][1]
        total.append([year, sumc])
        now += 1
    yeardep[len(yeardep) - 1][1] = startvals[len(startvals) - 1][1]
    total[len(total) - 1][1] = costinit
    return [startvals, yeardep, total]
    
def format(array, times):
    for i in xrange(times):
        print str(array[0][i][0]) + "\t" + str(array[0][i][1]) + "\t" + str(array[1][i][1]) + "\t" + str(array[2][i][1])
    
    
def go():
    name     = str(raw_input("What is the item?: "))
    start    = int(raw_input("What year was it purchased?: "))
    price    = float(raw_input("What was the initial price?: "))
    lifetime = int(raw_input("Estimated lifetime?: "))
    method   = int(raw_input("Method of depreciation? (0 for SL 1 for DDB): "))
    
    answers = getDep(start, price, lifetime, method)
    print "Printing chart for item: " + str(name)
    print "Year\tValue At Start of Year\tDepreciation\tTotal Depreciation"
    format(answers, len(answers[0]))
    
go()
	    
