#8
#https://learnpythonthehardway.org/book/ex8.html

#define formatter as a string comprised of 4 variables
formatter = "%r %r %r %r"

#print formatter and set the 4 variables as integers
print formatter % (1, 2, 3, 4)
#print formatter and set the 4 variables as strings
print formatter % ("one", "two", "three", "four")
#print formatter and set the variables as boolean
print formatter % (True, False, False, True)
#print formatter and set the variables...hmm not sure what this does
print formatter % (formatter, formatter, formatter, formatter)
#aah i see it actually uses formatter as a variable that contains a string
#that is because of the string format being %r which prints exactly what is written

#print formatter and set the 4 variables as strings again.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
