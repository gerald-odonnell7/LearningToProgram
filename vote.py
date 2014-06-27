age = input("How old are you?")
citizen = raw_input("Are you a citizen [Y/N]")
if(age>=18 and citizen=="Y"):
	print "You are eligible to vote"
	print "Please enter the voting booth."
else:
	print "You are not eligible to vote."

