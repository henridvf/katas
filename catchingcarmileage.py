def is_interesting(number, awesome_phrases):
    
    # code = 0

    # 3 or more digits
    if number <= 99: return 0

    # put dummy value in awesome_phrase
    # if len(awesome_phrases) == 0: awesome_phrases.append(-1)

    # interesting numbers
    # all same digits
    if len(set(number) == 1): return 2

    # nearing a provided "awesome phrase"
    for n in awesome_phrases:
        if number == n: 
            return 2
        elif (number >= n - 2) and (number < n):
            return 1
        else:
            return 0
    
    # check if palindrome
    if str(number) == str(number)[::-1]:
        return 2
    elif str(number+1) == str(number+1)[::-1]:
        return 1
    elif str(number+2) == str(number+2)[::-1]:
        return 1
    else:
        return 0


# print(is_interesting(3, [1337, 256]))