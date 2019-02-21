from sys import argv
from os.path import exists

script, from_file, to_file = argv


#in_file = open(from_file)
indata = open(from_file).read()


out_file = open(to_file, 'a')
out_file.write(indata)

print "Alright, all done. Appended all contents."

out_file.close()
#in_file.close()