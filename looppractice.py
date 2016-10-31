
days= ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
#for i in range(15):

t=2

while(t != 1):

	question = raw_input("Press 1 for workweek or Press 2 to see the whole week, for weekends press 3, Press 5 to exit")

	if (int(question) == 1):
		i=1
		while(i<6):
			print days[i]
			i=i+1
	elif(int(question)==2):
		i=0
		while(i<7):
			print days[i]
			i=i+1
	elif(int(question)==3):
		i=0
		for i in [0,6]:
			print days[i]
	elif(int(question)==5):
		t=1
	else:
		print "Invalad response please select again"
		print ""
		print ""
		print ""
		
