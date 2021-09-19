import pytest
import katas.zerosandones as kt 


def test_replace_zero_1():
    assert kt.replace_zero([1,1,1,0,1,1,0,1,1,1]) == 6

def test_replace_zero_2():
    assert kt.replace_zero([0,1,1,1]) == 0

def test_replace_zero_3():
    assert kt.replace_zero([1,1,1,0]) == 3

def test_replace_zero_4():
    assert kt.replace_zero([1,1,1,0,0,1,1,1,1,1,0,1]) == 10

def test_replace_zero_5():
    assert kt.replace_zero([0,1,0,0,0,0]) == 2

def test_replace_zero_6():
    assert kt.replace_zero([0,0,0,0,0,1]) == 4

def test_replace_zero_7():
    assert kt.replace_zero([0,0,0,0,1,0]) == 5

def test_replace_zero_8():
    assert kt.replace_zero([1,0,0,0,0,0]) == 1
