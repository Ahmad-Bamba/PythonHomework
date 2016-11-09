# Population Growth
# Ahmad Bamba
# 9/16/2016

population = 7.0 # billion
years = 0 # after 2011
rate = .011 # 1.10%

while population < 8.0:
    population = population + (population * rate)
    # print "Debug: " + str(population)
    years += 1

print "The population will reach 8 billion in: " + str(2011 + years)
