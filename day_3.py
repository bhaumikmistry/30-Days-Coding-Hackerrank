#day2 operators

mealCost = float(raw_input())
tipPercentage = int(raw_input())
taxPercentage = int(raw_input())

tip = mealCost * float(tipPercentage)/100
print tip
tax = mealCost * float(taxPercentage)/100
print tax

totalCost = round(mealCost + tip + tax)

print "The total meal cost is %d dollars" % totalCost
