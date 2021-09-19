import pytest
import katas.catchingcarmileage as kt 


def test_is_interesting_1():
    assert kt.is_interesting(1335, [1337, 256]) == 1

def test_is_interesting_2():
    assert kt.is_interesting(1336, [1337, 256]) == 1

def test_is_interesting_3():
    assert kt.is_interesting(1337, [1337, 256]) == 2


# progress as we near an "interesting" number
def test_is_interesting_4():
    assert kt.is_interesting(11207, []) == 0

def test_is_interesting_5():
    assert kt.is_interesting(11208, []) == 0

def test_is_interesting_6():
    assert kt.is_interesting(11209, []) == 1

def test_is_interesting_7():
    assert kt.is_interesting(11210, []) == 1

def test_is_interesting_8():
    assert kt.is_interesting(11211, []) == 2

def test_is_interesting_9():
    assert kt.is_interesting(3, [1337, 256]) == 0

def test_is_interesting_10():
    assert kt.is_interesting(3236, [1337, 256]) == 0