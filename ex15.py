#ex15
#https://learnpythonthehardway.org/book/ex15.html
#For now just understand that sys is a package, and this phrase just
#says to get the argv feature from that package. You'll learn more
#about these later.
from sys import argv
#unpacking argv: first argument is the name of the script then second
#is the file with the text we are opening
script, filename =argv
#open filename and assign to txt variable
txt = open(filename)
#print name of file
print "Here's your file %r:" % filename
# using function read with no parameters print the content of txt
print txt.read()
#ask user for filename again
#print "Type the filename again:"
#file_again = raw_input("> ")
#open the file and assign content to txt_again
#txt_again = open(file_again)
#call read() on the txt_again variable
#print txt_again.read()
