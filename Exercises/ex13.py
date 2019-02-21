from sys import argv

script, first, second, third = argv

print "This script is called:", script
print "Your first name is:", first
print "Your middle name is:", second
print "Your last name is:", third


print "\n \n \n ---------------------------"
print "\n \n \n "

town = raw_input("Where you live?")


print "\n\n So, Your full name is: %s %s %s and you live in %s" % (first, second, third, town) 
