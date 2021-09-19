import pytest
import katas.listfiltering as kt 


def test_filter_list_1():
    assert kt.filter_list([1,2,'a','b']) == [1,2]

def test_filter_list_2():
    assert kt.filter_list([1,'a','b',0,15]) == [1,0,15]

def test_filter_list_3():
    assert kt.filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
    