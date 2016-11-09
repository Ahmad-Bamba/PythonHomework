# Credit Card
# Ahmad Bamba
# 10/04/2016

user = str(raw_input("Enter number"))

digits = []

for char in user:
	digits.append(int(char))

doubles = []

for i in xrange(0, len(digits) - 1, 2):
	if (digits[i] * 2) >= 10:
		doubles.append((digits[i] * 2) - 9)
	else:
		doubles.append(digits[i] * 2)

sum1 = sum(doubles)
sum2 = sum(digits[1::2])

if(sum1 + sum2) % 10 == 0:
	print "ACCEPTED"
else:
	print "REJECTED"
