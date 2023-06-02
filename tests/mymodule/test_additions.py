import pytest
import math

from myapp.mymodule.funcs import add


@pytest.mark.parametrize("a, b, c", [(10,20, 30), (20,40,60), (11,22,33)])
def test_add(a, b, c):
    res = add(a, b)
    print(res)
    assert res == c

@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100 # it will fail now


@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100


@pytest.mark.others
def test_less():
   num = 100
   assert num < 200


@pytest.mark.square
def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

@pytest.mark.square
def testsquare():
   num = 7
   # assert 7*7 == 40  #n ** 2
   assert pow(num, 2) == 40

@pytest.mark.others
def test_equality():
    assert 10 == 11