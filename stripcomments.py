def solution(string,markers):
    
    sol = ''
    lst = string.splitlines()
    
    for line in lst:
        # find positions of all possible markers in a line
        lst_occ = [pos for pos, char in enumerate(line) if char in markers]
        # if any markers found
        if len(lst_occ) > 0:
            # slice line up to the first marker
            sol += line[:lst_occ[0]].strip() + '\n'
        else:
            sol += line + '\n'

    return sol[:-1]



# print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
print(solution("avocados apples apples , ?\navocados\n' apples ?\n= ^\n! lemons", ['@', '^', '-', '!', "'", '?']))
