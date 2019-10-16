# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 21:23:20 2019

@author: Jos
"""
#%%
import re
from reprlib import repr

pat = re.compile(r'\w+')

class Sentence:
    
    def __init__(self, text):
        self.text = text
        #self.words = pat.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % repr(self.text)

    def __iter__(self):
        for match in pat.finditer(self.text):
            yield match.group()

        return
#%%    
    
def gen():
    while True:
        try:
            yield 2
        except GeneratorExit:
            yield 3
            
#%%
import logging
def countdown(n):
    logging.debug("Counting down")
    while n > 0:
        try:
            yield n
        except GeneratorExit:
            logging.error("GeneratorExit")
        n -= 1


#if __name__ == '__main__':
c = countdown(10)
logging.debug("value: %d", next(c))