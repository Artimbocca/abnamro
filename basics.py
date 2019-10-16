# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:44:16 2019

@author: Jos
"""
#%%
a = [1,2,3,'b']
a[2]
a[1:3]='a'
a; a[::-1]
a[-1:0:-1]
a[2:]


import io
buf = io.StringIO()


def foo(x):
    try:
        return 3/x
    except ZeroDivisionError:
        print('Zero')
    finally:
        print('Poeh')
    #else:
        #print('esle')
        

class Foo:
    def __init__(self, a):
        self.a = a
    def baz (self):
        return self.a

#%%
class A: pass

class B(A): pass

class C(B, AF): pass


