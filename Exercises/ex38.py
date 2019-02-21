ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

#sentence ten_things is splitted and copied to stuff in a list format
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

print "\n" , stuff , "\n"
print "Length of stuff:", len(stuff), '\n'

#while loop with a condition length of stuff is not equal to 10
while len(stuff) != 10:
	#pop() pops out last element from a list and returns, here in next_one
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	#values from pop() function are appended to stuff
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

#as in python count starts with 0, first element in stuff is printed
print stuff[1]
#last element from stuff is printed
print stuff[- 1] # whoa! fancy
#last element is popped out from list stuff
print stuff.pop()
#list elements from stuff are joined all together to form as a string with 
#connecting string as ' ' (blank space)
print ' '.join(stuff) # what? cool!
#elements 3rd and 4th (3:5 means third element and 5-1st element) are joined together with #
print '#'.join(stuff[3:5]) # super stellar!