# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:50:52 2019

@author: Jos
"""

def singleton(cls):
    instances = {}
    def wrapped(*args):
        if cls not in instances:
             instances[cls]=cls(*args)
        return instances[cls]
    return wrapped

@singleton
class Foo: pass
@singleton
class Baz: pass

#%%

class Singleton(type):
  instance = None
  def __call__(cls, *args, **kwargs):
    if not cls.instance:
      cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
      # or just: cls.instance = super().__call__(*args, **kwargs)
    return cls.instance
class ASingleton(metaclass=Singleton):
  pass

a = ASingleton()
b = ASingleton()
a is b   


#%%
class Singleton: 
    _instance = None 
    def __new__(cls, *args, **kwargs): 
        if not cls._instance: 
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance 
        
Singleton() is Singleton()



