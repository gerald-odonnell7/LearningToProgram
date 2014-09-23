family = ['Adam', 'Jill', 'Jack', 'Paul', 'Tom', 'Wilma']
age = [50, 40, 30, 20, 25, 45]
gpa = [3.44, 2.7, 2.9, 3.2, 4.0, 3.98]

x = 0
total = 0
while x < 6:
	print family[x], ' is ', age[x], ' years old and the gpa is ', gpa[x]
	total = total + gpa[x]
	x = x + 1

print "Total number of gpa's", x
print 'The average gpa is', total / x


age[3] = 21

print age

print gpa
del gpa[1]
print gpa
