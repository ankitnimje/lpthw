# Refer to https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# for more details regarding python Input/output

from sys import argv

script , filename = argv

print "We're going to erase %s." % filename
print "if you don't wan that, hit CTRL-C (^C)."
print "If you want that, hit RETURN."

#It is used to proceed. CTRL-C giving error and jumping out. Hitting RETURN would proceed.
raw_input('>>>')

print "Opening the file... %s" % filename
#open file with write access or write parameter so file can be modified
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
#Erases everything on the file
target.truncate()

print "Now I'am going to ask you for three lines."

line1 = raw_input("Line 1 >>> ")
line2 = raw_input("Line 2 >>> ")
line3 = raw_input("Line 3 >>> ")

print "I'm going to write these to the file."

#Writing lines one by one onto the file. 
#\n Helps next line after each line to keep it neat.
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

#Not ssure how to read this file
#readLine = open(filename)
#print filename.read()

print "And finally we close file."
target.close()