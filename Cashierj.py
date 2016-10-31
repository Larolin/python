y= (float(raw_input("Input dollar amount: ")))
y= int(y*100+.5)
print "you have ", (y) , "pennies worth"
print "Quarters: ", (y/25)
quarters=y%25
dimes=quarters%10
print "Dimes: ", (quarters/10)
nickels=dimes%5
print "Nickels: ", (dimes/5)
pennies=nickels%1
print "Pennies: ", (nickels/1)
