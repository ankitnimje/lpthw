print "Enter a loop iteration"
j = int(raw_input('>>'))
i = 0
numbers = []

while i < j:

	print "--" * 10
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	print "Numbers now: ", numbers

	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num