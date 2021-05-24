import pytest
import sys
from main import *


@pytest.mark.skipif(sys.version_info.major == 2, reason='Python2-de islemir')
def test_division():
    assert division(1,2)==0.5

def test_division_fail():
    assert division(1,0)== 1

@pytest.mark.xfail(strict=True)
def test_division_fail2():
    assert division(1,3)== 1

#@pytest.mark.xpass
#def test_division_fail3():
#    assert division(1,2)== 1

@pytest.mark.parametrize("a,b",[(1,2),(2,1),(3,1),(4,1)])
def test_division_param(a,b):
    assert division(a,b)==a/b


def test_fix(structure):
    print('from test_fix')
    assert isinstance(structure.text, str)
    assert isinstance(structure.num,int)

def test_obj_number(structure):
    print('from test_obj_number')
    assert structure.num == 10

def test_obj_number2(structure2):
    print('from test_obj_number2')
    assert structure2.num == 11


def test_obj_number3(structure2):
    print('from test_obj_number2')
    assert structure2.num == 11