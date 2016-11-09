# Bouncing Ball
# Ahmad Bamba
# 9/16/2016

def getResult(c, h):
    # starts after the first bounce
    # print "Debug: " + str(c) + " " + str(h)
    bounces = 1
    currentHeight = h
    subtotal = h
    
    while True:
        # print "Debug: " + str(bounces) + " " + str(currentHeight * c)
        currentHeight *= c
        if(currentHeight <= .1):
            break
        subtotal += currentHeight
        bounces += 1

    total = ((subtotal - h) * 2) + h
    return [bounces, total]

ball = int(raw_input("What type of ball will you bounce? (Tennis ball - 0, Basketball - 1, Super Ball - 2, Soft ball 3): "))
height = float(raw_input("What height (in meters) are you dropping the ball from?: "))
# keys the name of the ball to the coefficient of resitution given
cordict = { 'tennis': 0.7, 'basket': 0.75, 'super': 0.9, 'soft': .3 }

if ball == 0:
    result = getResult(cordict['tennis'], height)
    print "The number of times this ball bounced before bouncing less than 10cm is: " + str(result[0]) + " times."
    print "The total distance travelled by the ball is: " + str(round(result[1], 2)) + "m"
elif ball == 1:
    result = getResult(cordict['basket'], height)
    print "The number of times this ball bounced before bouncing less than 10cm is: " + str(result[0]) + " times."
    print "The total distance travelled by the ball is: " + str(round(result[1], 2)) + "m"
elif ball == 2:
    result = getResult(cordict['super'], height)
    print "The number of times this ball bounced before bouncing less than 10cm is: " + str(result[0]) + " times."
    print "The total distance travelled by the ball is: " + str(round(result[1], 2)) + "m"
elif ball == 3:
    result = getResult(cordict['soft'], height)
    print "The number of times this ball bounced before bouncing less than 10cm is: " + str(result[0]) + " times."
    print "The total distance travelled by the ball is: " + str(round(result[1], 2)) + "m"
else:
    print "[Error] In valid ball type!"
