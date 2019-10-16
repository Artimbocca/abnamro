# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:46:11 2019

@author: jos
"""

from functools import wraps
def debug(func):
    
    msg = func.__qualname__
    @wraps(func)
    def wrapped(*args, **kwargs):
        print("In: "+ msg)
        return func(*args, **kwargs)
    return wrapped


def debugmethods(cls):
    for name, val in vars(cls).items():
        if callable(val):
            setattr(cls, name, debug(val))
    return cls

class Foo:
    @debug
    def baz(self): pass

    @staticmethod
    def static(): pass

    @classmethod
    def classm(cls): pass

def debugattr(cls):
    orig_getattribute = cls.__getattribute__
    def __getattribute__(self, name):
        print('Get:', name)
        return orig_getattribute(self, name)
    cls.__getattribute__ = __getattribute__
    return cls

class debugmeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsobj = super().__new__(cls, clsname, bases, clsdict)
        clsobj = debugmethods(clsobj)
        return clsobj