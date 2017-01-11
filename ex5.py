#ex5
#https://learnpythonthehardway.org/book/ex5.html

#define variables
my_name = 'I. Pop'
my_age = 29 #as of yesterday
my_height = 1.80 #meters
my_weight = 70 #kg
my_eyes = 'Brown'
my_teeth = 'invisalign'
my_hair = 'Brown'

#out put some phrases that use format string that embeds variables
print "Let's talk about %s." % my_name
print "He's %f meters tall." % my_height
print "He's %f kilograms heavy." % my_weight
print "Actually thats not too heavy."
print "He's go %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth usually have %s trays on depending on if he's drinking coffee or not." % my_teeth

#this line is tricky, try to get it exactly right and just now you realize that
#you are just copying random things from another page instead of copy/paste LOL
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

#PART 2 of ex5 cleans things up a bit
#also some math to convert m/kg to inch/lbs
#See all python format characters here: https://docs.python.org/2.4/lib/typesseq-strings.html

#define variables
name = 'I. Pop'
age = 29 #as of yesterday
height = 1.80 #meters
weight = 70 #kg
eyes = 'Brown'
teeth = 'invisalign'
hair = 'Brown'

#out put some phrases that use format string that embeds variables
print "Lets try this again but now with imperial numbers"
print "Let's talk about %s." % name
print "He's %f inches tall." % (height * 12 * 2.54)
print "He's %f pounds heavy." % (weight * 2.2)
print "Actually thats not too heavy."
print "He's go %s eyes and %s hair." % (eyes, hair)
print "His teeth usually have %s trays on depending on if he's drinking coffee or not." % teeth

print "If I add %d, %f (meters) and %d (kilograms), I get %d." % (age, height, weight, age + height + weight)
print "We are going to convert that to imperial:"
print "If I add %d, %f (inches) and %d (pounds), I get %f." % (age, height * 12 * 2.54, weight * 2.2, age + (height * 12 * 2.54) + (weight * 2.2))

print "lets try other format characters"
print "%r is %d old and has %s hair. He weighs %d kilos and is %r meters tall." % (name, age, hair, weight, height)
print "The answer to the ultimate question is %r." %(round (weight - age + height))
print "Whooops seems we rounded wrong, lets try that again."
print "The answer to the ultimate question is %d." % (int(weight - age + height))
