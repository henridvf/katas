import pytest
import katas.greedisgood as kt 


def test_score_1():
    assert kt.score( [2, 3, 4, 6, 2] ) == 0

def test_score_2():
    assert kt.score(  [4, 4, 4, 3, 3] ) == 400

def test_score_3():
    assert kt.score(  [2, 4, 4, 5, 4] ) == 450