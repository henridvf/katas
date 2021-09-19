import pytest
import katas.stripcomments as kt 


def test_solution_1():
    assert kt.solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]) == "apples, pears\ngrapes\nbananas"

def test_solution_2():
    assert kt.solution("a #b\nc\nd $e f g", ["#", "$"]) == "a\nc\nd"

def test_solution_3():
    assert kt.solution('# lemons strawberries\nwatermelons\nstrawberries avocados\nwatermelons lemons oranges strawberries pears\napples', ['^', '?', '-', '!', '#', '.']) == '\nwatermelons\nstrawberries avocados\nwatermelons lemons oranges strawberries pears\napples'

def test_solution_4():
    assert kt.solution('! apples watermelons avocados avocados\nlemons pears\nstrawberries oranges lemons . watermelons bananas\napples strawberries . cherries lemons', ['!', '.', '-', '?', ',', '@']) == '\nlemons pears\nstrawberries oranges lemons\napples strawberries'

def test_solution_5():
    assert kt.solution(', bananas . watermelons oranges =\napples cherries cherries avocados pears\navocados bananas\navocados\ncherries avocados', ['@', "'", '-', '^', ',', '=', '#']) == '\napples cherries cherries avocados pears\navocados bananas\navocados\ncherries avocados'

def test_solution_6():
    assert kt.solution('! oranges\navocados oranges\nbananas pears apples strawberries\napples strawberries pears\nbananas . apples', ['-', ',', '!', '@', '.', '#', '?', "'", '^']) == '\navocados oranges\nbananas pears apples strawberries\napples strawberries pears\nbananas'

def test_solution_7():
    assert kt.solution('=\navocados\n# - cherries @ ,\n^ , oranges watermelons pears\napples ! avocados', ['^', '#', ',', "'", '-', '=']) == '\navocados\n\n\napples ! avocados'

def test_solution_8():
    assert kt.solution("avocados apples apples , ?\navocados\n' apples ?\n= ^\n! lemons", ['@', '^', '-', '!', "'", '?']) == 'avocados apples apples ,\navocados\n\n=\n'

def test_solution_9():
    assert kt.solution('cherries\nlemons oranges apples oranges lemons\nbananas\npears oranges\n, ? cherries lemons watermelons', ['^', ',', '.', "'"]) == 'cherries\nlemons oranges apples oranges lemons\nbananas\npears oranges\n'