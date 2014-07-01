#tuples are identified by parenthesis
subjects = ('physics', 'chemistry', 'algebra', 'gym', 'biology')
classrooms = (101, 107, 210, 0, 109)
print subjects
print subjects[0]

#immutable list cannot be changed
#subjects[2] = 'latin'

#tuples may use functions
print 'Highest classroom number', max(classrooms)
print 'Lowest classroom number', min(classrooms)


