import pytest
from main import *

@pytest.fixture(scope="module")
def structure():
    print('from structure')
    my_obj = MyStruct(10)
    yield my_obj
    print('tear down')
    del my_obj


@pytest.fixture
def structure2():
    print('from structure2')
    my_obj = MyStruct(11)
    yield my_obj
    print('tear down structure2')
    del my_obj