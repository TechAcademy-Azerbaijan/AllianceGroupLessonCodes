# import pytest

def division(a,b):
    try:

        return a/float(b)
    except ZeroDivisionError:
        return 1

division(1,1)


class MyStruct(object):
    text = ""

    def __init__(self, num):
        self.num = num
     

