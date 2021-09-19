import pytest
import katas.calculatingwithfunctions as kt 


def test_domain_name_1():
    assert kt.seven(kt.times(kt.five())) == 35
    assert kt.four(kt.plus(kt.nine())) == 13
    assert kt.eight(kt.minus(kt.three())) == 5
    assert kt.six(kt.divided_by(kt.two())) == 3