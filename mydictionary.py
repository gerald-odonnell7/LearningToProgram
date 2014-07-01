#a dictionary is identified by squiggly bracketkets
classes = {"physics" : 101, "chemistry" : 107, "algebra" : 210, "gym" : 0, "biology" : 109}
print classes
print "Algebra meets in room: ", classes["algebra"]

#change a value
classes["algebra"] = 211
print "Algebra has moved to room: ", classes["algebra"]

#delete an item
print classes
del classes["gym"]
print classes

#check for a key
if classes.has_key("algebra"):
	print "You have algebra scheduled"
if classes.has_key("gym"):
	print "You have gym scheduled"

print classes.keys()
print classes.values()
