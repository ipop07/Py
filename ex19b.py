#caesar cyper

import string; f = lambda s, n: ''.join([string.ascii_lowercase[string.ascii_lowercase.index(c) + n % 26] for c in s]); print f('xyz', 3)

#def caesar(s, n):
#    import string
#    for c in s:
#        if string.ascii_lowercase.index(c) == (' '):
#            f = unichr(32)
#        else:
#            f = string.ascii_lowercase[string.ascii_lowercase.index(c) + n % 26]
#        print f,
#
#caesar('ab c', 3)
