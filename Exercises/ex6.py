x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#Printing x with quotes since we are using %r here which preserves quotes
print "I said: %r." % x

#printing without quotes (uses extra quotes given below)
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#using %r from string joke_evaluation which preserves %
print joke_evaluation % hilarious
w = "This is the left side of..."
e = "a string with a right side."

print w + e