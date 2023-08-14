# coding = UTF8

"""
单例模式

使用方法：
class Foo(metaclass=SingletonType):
  def __init__(self):
    pass

test1 = Foo()
test2 = Foo()
assert id(test1) == id(test2)
"""

import threading

class SingletonType(type):
  _instance_lock = threading.Lock()
  def __call__(cls, *args, **kwargs):
    if not hasattr(cls, "_instance"):
      with SingletonType._instance_lock:
        if not hasattr(cls, "_instance"):
          cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
    return cls._instance
