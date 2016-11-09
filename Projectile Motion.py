# Projectile Motion
# Ahmad Bamba
# 10/12/2016

def maxHeight(h, v):
    return h + v * (v/32) - 16 * ((v/32) ** 2)

def calcGroundTime(h, v):
    t = 0.0
    found = 0.0
    running = True
    while running:
        if (h + v * t - 16 * (t ** 2)) < 0:
            running = False
            found = t
        t += .1
    return found

def sanitize(number):
    if number <= 0:
        return False
    return True
        
def getInput():
    user_height = float(raw_input("What was the initial height of the ball?: "))
    user_velocity = float(raw_input("What was the initial velocity of the ball?: "))

    if not sanitize(user_height) or not sanitize(user_velocity):
        print "Invalid input!"
    else:
        print "The maximum height of the ball is: " + str(round(maxHeight(user_height, user_velocity), 3)) + " feet."
        print "The ball hits the ground after approximately: " + str(round(calcGroundTime(user_height, user_velocity), 3)) + " seconds."

getInput()
