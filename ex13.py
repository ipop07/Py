#ex13
#https://learnpythonthehardway.org/book/ex13.html

from sys import argv

script, first, second, third = argv

prefix = raw_input("what?: ")
print "The script is called:", script
print "Your first variable is:", prefix, first
print "Your second variable is:", second
print "Your third variable is:", third
