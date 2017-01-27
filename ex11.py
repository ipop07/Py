#ex11
#https://learnpythonthehardway.org/book/ex11.html


print "How old are you?",
age = int(raw_input())
print "How tall are you?",
height = int(raw_input())
print "How much do you weigh?",
weight = raw_input()

print "so, you are %r old, %r tall and %r heavy." % (age, height, weight)

print "Halt!"
s = raw_input("Who Goes there? ")
print "You may pass,", s


age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "so, you are %r old, %r tall and %r heavy." % (age, height, weight)
