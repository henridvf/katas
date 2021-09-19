import pytest
import katas.dubstep as kt 


# "WUB should be replaced by 1 space"
def test_song_decoder_1():
    assert kt.song_decoder("AWUBBWUBC") == "A B C"

# "multiples WUB should be replaced by only 1 space"
def test_song_decoder_2():
    assert kt.song_decoder("AWUBWUBWUBBWUBWUBWUBC") == "A B C"

# "heading or trailing spaces should be removed"
def test_song_decoder_3():
    assert kt.song_decoder("WUBAWUBBWUBCWUB") == "A B C"