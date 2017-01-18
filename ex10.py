#Ex10
#https://learnpythonthehardway.org/book/ex10.html

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "Lets try some more."

var1 = "I \aam intrigued with the ASCII bell (BEL)"
var2 = "I \bam really intrigued with the ASCII backspace (BS)"
var3 = "I \fam a litle confused with ASCII formfeed (FF)"
var4 = "I \N{name}, think this is a lot to learn about names"
var5 = "this is a \r carriage return"
var6 = "I know what a \t horizontal tab does"
var7 = "I think I might know what a \v vertical ASCII tab does"
var8 = "what is \123 octal value 123"
var9 = "I have a feeling this character hex \xA1 A1 has some important meaning"

print var1
print var2
print var3
print var4
print var5
print var6
print var7
print var8
print var9

x = 0
while True:
    if x == 1000000:
        break
    else:
        x += 1
        for i in ["/","-","|","\\","|"]:
            print "%s\r" % i,

print "what the crap just happened? I think I know lets try that bamboozle again"
x=0
while True:
    if x == 1000000:
        break
    else:
        x += 1
        for i in ["this","is","a","statement","that","is","useless"]:
            print "%s \r" % i,

print "this is the end (Adele)"
