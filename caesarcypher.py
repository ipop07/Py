#caesar cypher

#import string; f = lambda s, n: ''.join([string.ascii_lowercase[(string.ascii_lowercase.index(c) + n) % 26] for c in s]); print f('xyz', 3)

from sys import argv
script, offset = argv
prompt = 'Phrase to (de)cypher > '
#phrase to convert
codephrase = raw_input(prompt)
#output to file or just print
fileoutput = raw_input('Do you want to save this to a file? Y/N ')

#if output to file, open file and truncate
if fileoutput in ('Y', 'y'):
    target = open('caesarcypher.txt', 'w')
    target.truncate()
#function which replaces each character
#by one with a pre-determined ASCII value offset
def caesar(s, n):
    #open string module
    import string
    #for each character in s find the ascii code and offset by n
    for c in s:
        #if character is a letter
        if c in string.ascii_letters:
            f = string.ascii_letters[(string.ascii_letters.index(c) + n) % 26]
        else:
            #if its not a letter find the ascii code and offset by n
            f = chr(ord(c) + n)
        print f,
        #append to the file if fileoutput was yes
        if fileoutput in ('Y', 'y'):
            target.write("%s" % f)
#call caesar function
caesar(codephrase, int(offset))
