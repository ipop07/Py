#ex16
#https://learnpythonthehardway.org/book/ex16.html

from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print "If you dont want that hit N"
print "If you do want that hit Y"

answer = raw_input("?")

if answer in ('Y','y'):
    print "Opening file..."
    target = open(filename, 'w')

    print "truncating the file. Goodbye!"
    target.truncate()

elif answer in ('N','n'):
    print "Adding lines at end of file."
    target = open(filename, 'a')
else:
    print "Invalid input. Exiting."
    raise SystemExit #exits program
print "Now I'm going to ask for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
target.write("%s \n%s \n%s \n" % (line1, line2, line3))

print "And finally, we close it."
target.close()
