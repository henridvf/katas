import pytest
import katas.roman_numerals as kt


def test_domain_name_1():
    assert kt.RomanNumerals.to_roman(1000) == 'M'
    # '1000 should == "M"')
# test.assert_equals(RomanNumerals.to_roman(1990), 'MCMXC', '1990 should == "MCMXC"')
#
# test.assert_equals(RomanNumerals.from_roman('XXI'), 21, 'XXI should == 21')
# test.assert_equals(RomanNumerals.from_roman('MMVIII'), 2008, 'MMVIII should == 2008')