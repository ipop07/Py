#ex6
#https://learnpythonthehardway.org/book/ex6.html

#define variables and lets make them fun
#define a variable as a string
x= "there are %d types of people." %10
binary = "binary"
do_not = "don't"
#define a variable as a string that contains 2 other variables defined earlier
y = "Those who know %s and those who know %s." % (binary, do_not)

#print variables
print x
print y
#print message that includes variable x and then another with variable y
print "I said: %r." % x
print "I also said: '%s'." % y
#define a string variable
hilarious = False
joke_evaluation = "Isn't tht joke so funny?! %r"
#print 2 variables on the same line
print joke_evaluation % hilarious

#repeat the same thing we just did but with string variables
w = "This is the left side of..."
e = "a string with a right side."
print w + e
