# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 21:32:40 2019

@author: Jos
"""

def init_Foo(self, name):
    self.name = name
    
Foo2 = type("Foo",
            (),
            {"a":0,
             "__init__": init_Foo,
             "baz": lambda self: "baz"})
    
foo = Foo2('a foo')


class controlled_execution:
    def __enter__(self):
        print("Entering")
        self.x = 2
        return self 
    def __exit__(self, exc, val, traceback): 
        print("Leaving")
        del self.x

with controlled_execution() as thing: 
     print(thing.x)

