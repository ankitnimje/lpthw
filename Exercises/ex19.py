'''
#defining a function cheese_and_crackers with two parameters cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "\nYou have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
print "Direct passing of function values:"
#calling a function cheese_and_crackers with values 20 and 30
cheese_and_crackers(20, 30)

print "Passing values using varible values:"
amount_of_cheese = 10
amount_of_crackers = 50

#calling cheese_and_crackers with two values as variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can pass math values too:"
cheese_and_crackers(10+20, 5+6)

print "We can also combine variable and maths:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
'''

print "-------------------------------------------------------"
print "-------------------------------------------------------"

def call_me(one, two, three):
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\nAddition is: %d" % (one + two + three)
	print "\nSubtraction is: %d" % (one - two - three)
	print "\nProduct is: %d" % (one * two * three)


#Used INT(RAW_INPUT(.......)) to convert string input value to int
first = int(raw_input("1st value >>> "))
second = int(raw_input("2nd value >>> "))
third = int(raw_input("3rd value >>> "))
temp = 5

call_me(first, second, third)
call_me(100, 60, 30)
call_me(10 + 2, 12 - 5, 3 * 2)
call_me(100 - temp , 60 - temp , 30 - temp)
call_me(first - temp, second - temp, third - temp)
call_me(first / 2, second / 3, third / 4)
call_me(2 * first, 3 * second, 4 * third)
call_me(first % second, second % third, third % first)
call_me(first + second + third, first - second - third, first * second * third)
