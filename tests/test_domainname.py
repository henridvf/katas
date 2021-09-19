import pytest
import katas.domainname as kt 


def test_domain_name_1():
    assert kt.domain_name("http://google.com") == "google"
    assert kt.domain_name("http://google.co.jp") == "google"
    assert kt.domain_name("www.xakep.ru") == "xakep"
    assert kt.domain_name("https://youtube.com") == "youtube"

def test_domain_name_2():
    assert kt.domain_name("http://www.google.com") == "google"