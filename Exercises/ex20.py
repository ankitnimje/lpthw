#importing a library argv from package sys. This is useful for command line arguments
from sys import argv

#two command line args: script_name and input_file name
script, input_file = argv

#defining a function print_all which accepts 1 argument f and applies f.read() which makes print file contents
def print_all(f):
	print f.read()

# I am not sure whats goin on here	
def rewind(f):
	f.seek(0)

#defining a function print_a_line which accepts two arguments; 	
def print_a_line(line_count, f):
	#readline() reads and prints line by line. Each call readline() takes next line
	print line_count, f.readline()

#I believe, opening contents of input_file and copying to current_file which is a local variable which stores the file contents. Thats all I believe	
current_file = open(input_file)

print "\n First let print the whole file: \n"

#calling print_all which passes one value current_file; Its a file name to be passed 
print_all(current_file)

print "\n Now lets rewind. Like a mixtape: \n"

#Not sure
rewind(current_file)

print "\n Lets print three line by line: \n"

current_line = 1
print_a_line(current_line, current_file) #current_line=1

#we are incrementing current_line just for presentation purpose
current_line += 1
print_a_line(current_line, current_file) #current_line=2

current_line += 1
print_a_line(current_line, current_file) #current_line=3

#Answer for 2::: When we call print_a_line, we are passing two variables.
# First one belongs to function's 1st parameter and second belongs to second parameter.
# Thus current_line is equivalent to line_counnt