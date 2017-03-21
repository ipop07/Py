#caesar cypher

#import string; f = lambda s, n: ''.join([string.ascii_lowercase[(string.ascii_lowercase.index(c) + n) % 26] for c in s]); print f('xyz', 3)

from sys import argv
script, offset = argv
import string


prompt = 'Phrase to (de)cypher > '
#phrase to convert
codephrase = raw_input(prompt)
#output to file or just print
output_to_file = raw_input('Do you want to save this to a file? Y/N ')


#function which replaces each character by one with a pre-determined ASCII value offset
def caesar(to_convert, offset):
    #open string module
    #for each character in s find the ascii code and offset by n
    output_string = ""
    for c in to_convert:
        #if character is a letter
        if c in string.ascii_letters:
            f = string.ascii_letters[(string.ascii_letters.index(c) + offset) % 26]
        else:
            #if its not a letter find the ascii code and offset by n
            f = chr(ord(c) + offset)
        output_string += f
    return output_string

#call caesar function and assign return to textoutput variable
textoutput = caesar(codephrase, int(offset))
print textoutput

#if output to file, open file and truncate
#if fileoutput in ('Y', 'y'): less efficient than
if output_to_file in 'Yy':
    target = open('caesarcypher.txt', 'w')
    #target.write("%s" % textoutput) less efficient than
    target.write(textoutput)
    target.close()
#call caesar function
