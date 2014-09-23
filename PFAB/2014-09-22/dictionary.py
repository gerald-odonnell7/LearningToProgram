classes = { "physics" : 101, "chemistry" : 107, "algebra" : 210, "gym" : 0, "biology" : 109 }
print classes

print 'Algebra is meeting in room', classes["algebra"]

#change algebra assignment
classes["algebra"] = 211
print classes


#delete a class
print classes
del classes["gym"]
print classes


#checking keys if they exist
if classes.has_key("algebra"):
	print "You have algebra scheduled"


print classes.keys()
print classes.values()
