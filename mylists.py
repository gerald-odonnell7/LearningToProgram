family = ['Adam', 'Jill', 'Jack', 'Paul', 'Tom', 'Wilma']
age = [50, 40, 30, 20, 25, 45]
gpa = [3.44, 2.7, 2.9, 3.2, 4.0, 3.98]

#print one family member
print family[0]

#print all the items in the list
print family
print age
print gpa

#print a list
x = 0
total = 0
print 'Name, age, gpa'
while (x <= 5):
	print family[x], age[x], gpa[x]
	total = total + gpa[x]
	x = x + 1
print 'Average gpa', total/6

#out of range error
#print family[6]

#alter a list item
print gpa
gpa[3] = 2.3
print gpa

#delete a list item
print family
del family[2]
del gpa[2]
del age[2]
print family


#add a member using commands from https://docs.python.org/2/tutorial/datastructures.html
print family
family.append("Chris")
print family

#sort
print family
family.sort()
print family
