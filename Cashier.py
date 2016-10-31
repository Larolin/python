y= (float(raw_input("Input dollar amount: ")))
z=y
y= float(y*100)
z= int((z+1)*100-100)
print "you have ", y , "pennies worth"
print z
print "Quarters: ", (y/25)
quarters=y%25
dimes=quarters%10
print "Dimes: ", (quarters/10)
nickels=dimes%5
print "Nickels: ", (dimes/5)
pennies=nickels%1
print "Pennies: ", (nickels/1)
