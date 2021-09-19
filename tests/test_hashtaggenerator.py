import pytest
import katas.hashtaggenerator as kt 


# 'Expected an empty string to return False'
def test_generate_hashtag_1():
    assert kt.generate_hashtag('') == False 

# 'Expeted a Hashtag (#) at the beginning.'
def test_generate_hashtag_2():
    assert kt.generate_hashtag('Do We have A Hashtag')[0] == '#'

# 'Should handle a single word.'
def test_generate_hashtag_3():
    assert kt.generate_hashtag('Codewars') == '#Codewars'

# 'Should handle trailing whitespace.'
def test_generate_hashtag_4():
    assert kt.generate_hashtag('Codewars      ') == '#Codewars'

# 'Should remove spaces.'
def test_generate_hashtag_5():
    assert kt.generate_hashtag('Codewars Is Nice') == '#CodewarsIsNice'

# 'Should capitalize first letters of words.'
def test_generate_hashtag_6():
    assert kt.generate_hashtag('codewars is nice') == '#CodewarsIsNice'

# 'Should capitalize all letters of words - all lower case but the first.'
def test_generate_hashtag_7():
    assert kt.generate_hashtag('CodeWars is nice') == '#CodewarsIsNice'

# 'Should capitalize first letters of words even when single letters.'
def test_generate_hashtag_8():
    assert kt.generate_hashtag('c i n') == '#CIN'

# 'Should deal with unnecessary middle spaces.'
def test_generate_hashtag_9():
    assert kt.generate_hashtag('codewars  is  nice') == '#CodewarsIsNice'

# 'Should return False if the final word is longer than 140 chars.'
def test_generate_hashtag_10():
    assert kt.generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat') == False