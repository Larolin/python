import random
goal=random.randint(1,100)
x= int(raw_input("Guess the number: "))
while (x != goal):
	if x<goal: 
		print "Guess Higher!"
	elif x>goal:
		print "Guess Lower!"
	x=int(raw_input("Guess the number: "))
print "Congrats"
print ""
print ""
print ""
print "GlaDOs will bake a cake!"

