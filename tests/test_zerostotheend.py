import pytest
import katas.zerostotheend as kt 


def test_move_zeros_1():
    assert kt.move_zeros(
        [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]

def test_move_zeros_2():
    assert kt.move_zeros(
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def test_move_zeros_3():
    assert kt.move_zeros([0, 0]) == [0, 0]

def test_move_zeros_4():
    assert kt.move_zeros([0]) == [0]

def test_move_zeros_5():
    assert kt.move_zeros([]) == []