# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:04:35 2019

@author: Jos
"""

s = u"Αποκωδικοποίηση και κωδικοποίηση ελληνικού κειμένου"
b = bytes(s, encoding='utf-8') 
b = s.encode(encoding='utf-8')
s == b.decode(encoding='utf-8') 
print('{:}'.format(hex(ord(s[1]))))
print(f'a formatted string:{s[1:22]}')

print(f'{s[1]} named: \N{GREEK SMALL LETTER PI}, by number: \u03c0')

import re
s= 'a\nb\\c'
print(
      re.search(r'\\',s),
      re.search('\\.',s),  #re.search('\\',s),
      re.search('\\\\',s),
      sep='\n'
)

#%%

def baz(a, b, c=3): ...

def foo(a, *, b, c=3):
    print(a,b,c,)


#def foo2(a, /, b, c=3):
#    print(a,b,c,)

def search(item, coll):
    for i, x in enumerate(coll):
        if item == x:
            print("Found at:", i)
            break
    else:
        raise ValueError('Nothing found!')
#%%
def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i
                
def chain2(*iterables):
    for it in iterables:
        yield from it
        
#%%
import re
from reprlib import repr

pat = re.compile(r'\w+')

class Sentence:
    
#    def __init__(self, text):
#        self.text = text
#        self.words = pat.findall(text)
        
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % repr(self.text)

#    def __iter__(self):
#        for word in self.words:
#            yield word
#        return
    def __iter__(self):
        for match in pat.finditer(self.text):
            yield match.group()

    
    
sentence = Sentence("Αποκωδικοποίηση και κωδικοποίηση ελληνικού κειμένου")

#%%

ge = (2*x for x in range(1,5))
print (ge)       		# <generator object <genexpr> at ..>

print (next(ge)) 		# prints 2
print('='*10)
for i in ge:      		# prints 4, 6 and 8
    print (i)

