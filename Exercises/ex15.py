#It imports argv library/module from sys. argv accepts command line arguments from user
from sys import argv

#This line defines there are two command line arguments, one is script itself and second one is file name to be read
script, filename = argv

#This line i believe imports contents of filename to another file variable txt
txt = open(filename)

print "Here's your file - %r \n" % filename
#This line prints contents from txt which is a copy of filename
print txt.read()
close(filename)

print "Type your filename again:"
file_again = raw_input(">>>")

#This line does the same thing as above, it access filename given and copies content to txt_again
txt_again = open(file_again)

#same as above
print txt_again.read()
close(file_again)