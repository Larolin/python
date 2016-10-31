print "Hello, World" #This is a comment
var="bananas"
print var
x=5+5
y=x+2
print x,y,x+y
print "Is X equal to Y?" ,x==y #Commas are needed to seperate things from print
print "Is X Less than Y?", x<y
z=int(raw_input("Enter a Number:"))
if z<10:
	print "Your number is small"

elif z>10:
	print "Your number is biggerthan 10"

else: #else is a catchall
	print "You've picked the number 10"

i=0 #common symbol for 0

while i<=10:
	print i, i*i
	i= i+1


